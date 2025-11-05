# decrypt_verify_client.py

import click
import requests
import json
import os
import mimetypes


API_BASE_URL = "https://algo.quantumize.dev"


def decrypt_then_verify_file_client(encrypted_file: str, private_decryption_key: str, signature_file: str, public_verification_key: str, file_id: str, sign_algo_id: str, encrypt_algo_id: str, save_path: str = None):
    """
    Client function to communicate with the “decrypt and verify” API.
    Sends a file to be decrypted and then verified using selected algorithms.
    """
    try:
        with open(encrypted_file, "rb") as f1, open(signature_file, "rb") as f2, open(private_decryption_key, "rb") as f3, open(public_verification_key, "rb") as f4:
            files = {
                "encrypted_file": (
                    os.path.basename(encrypted_file),
                    f1,
                    mimetypes.guess_type(encrypted_file)[0],
                ),
                "private_decryption_key": (
                    os.path.basename(private_decryption_key),
                    f3,
                    mimetypes.guess_type(private_decryption_key)[0],
                ),
                "signature_file": (
                    os.path.basename(signature_file),
                    f2,
                    mimetypes.guess_type(signature_file)[0],
                ),
                "public_verification_key": (
                    os.path.basename(public_verification_key),
                    f4,
                    mimetypes.guess_type(public_verification_key)[0],
                )
            }

            data = {
                #"file": encrypted_file,
                #"signature": signature_file,
                "file_id": file_id,
                "sign_algo_id": sign_algo_id,
                "encrypt_algo_id": encrypt_algo_id,
            }

            print(f"Sending files '{os.path.basename(encrypted_file)}' and '{os.path.basename(signature_file)}' to API for combined operation...")
            print(f"   Decryption Algo ID: {encrypt_algo_id}, Verification Algo ID: {sign_algo_id}")

            response = requests.post(
                f"{API_BASE_URL}/verify-decrypt/", files=files, data=data
            )

            if response.status_code != 200:
                click.echo(f"API error: {response.text}")
                return False, f"API error: {response.text}", {}
            
            if "application/octet-stream" in response.headers.get("Content-Type", ""):
                if os.path.isdir(save_path):
                    output_file = os.path.join(save_path, "decrypted_verified_" + os.path.basename(encrypted_file).replace("FILE.PEM", ""))
                else:
                    output_file = save_path

                with open(output_file, "wb") as out_f:
                    out_f.write(response.content)
                message = f"File decrypted and verified successfully and saved to '{output_file}'"
                return True, message, {}
            else:
                try:
                    api_response = response.json()
                    return False, api_response.get("error", "Unexpected response from API"), {}
                except Exception as e:
                    return False, f"API communication error: {e}", {}

    except requests.exceptions.RequestException as e:

        print(f"❌ Error connecting to API or API returned an error: {e}")
        return False, f"API communication error: {e}", {}
    except json.JSONDecodeError:

        print(
            f"❌ Error decoding JSON response from API. Response text: {response.text if 'response' in locals() else 'No response'}"
        )
        return False, "Invalid JSON response from API", {}
    except Exception as e:
        #
        print(f"❌ An unexpected error occurred: {e}")
        return False, f"An unexpected error occurred: {e}", {}

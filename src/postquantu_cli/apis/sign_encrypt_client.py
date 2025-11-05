# sign_encrypt_client.py

import requests
import json
import os
import mimetypes


API_BASE_URL = "https://algo.quantumize.dev"


def sign_then_encrypt_file_client(file_path: str, file_id: str, sign_algo_id: str, encrypt_algo_id: str):
    """
    Client function to communicate with the “sign and encrypt” API.
    Sends a file to be signed and then encrypted using selected algorithms.
    """
    try:
        with open(file_path, "rb") as f:
            files = {
                "file": (
                    os.path.basename(file_path),
                    f,
                    mimetypes.guess_type(file_path)[0],
                )
            }

            data = {
                #"file": file_path,
                "file_id": file_id,
                "sign_algo_id": sign_algo_id,
                "encrypt_algo_id": encrypt_algo_id,
            }

            print(f"Sending file '{os.path.basename(file_path)}' to API for combined operation...")
            print(f"   Signing Algo ID: {sign_algo_id}, Encryption Algo ID: {encrypt_algo_id}")

            response = requests.post(f"{API_BASE_URL}/sign-encrypt/", files=files, data=data)
            response.raise_for_status()
            response_data = response.json()

            result = {
                "message": response_data.get("message", ""),
                "Encryption Details": {
                    "encrypted_file_name": response_data.get("encrypted_file_name", ""),
                    "encrypted_file_hash": response_data.get("encrypted_file_hash", ""),
                    "private_decryption_key_name": response_data.get("private_decryption_key_name", ""),
                    "private_decryption_key_hash": response_data.get("private_decryption_key_hash", ""),
                },
                "Signing Details": {
                    "signature_file_name": response_data.get("signature_file_name", ""),
                    "signature_file_hash": response_data.get("signature_file_hash", ""),
                    "public_verification_key_name": response_data.get("public_verification_key_name", ""),
                    "public_verification_key_hash": response_data.get("public_verification_key_hash", ""),
                }
            }
  
           
            return True, "Combined operation successful", result

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

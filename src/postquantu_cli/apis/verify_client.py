# src/postquantu_cli/apis/file_encryption.py

import requests
import os
import click

BASE_API_URL = "https://algo.quantumize.dev"

def verify_file_client(file_path: str, public_verification_key: str, file_id: str, algo_id: str, original_file: str, save_path: str = None):
    """ 
    Calls the PQC API to verify a file using the specified algorithm.
    """
    if not os.path.exists(file_path):
        return False, f"File not found: '{file_path}'", {}

    if not os.path.isfile(file_path):
        return False, f"Path is not a file: '{file_path}'", {}
    
    if not os.path.exists(public_verification_key):
        return False, f"Public key file not found: '{public_verification_key}'", {}
    
    if not os.path.isfile(public_verification_key):
        return False, f"Public key path is not a file: '{public_verification_key}'", {}

    endpoint = f"{BASE_API_URL}/verify/"

    try:
        if original_file:
            with open(original_file, "rb") as f1, open(file_path, "rb") as f2, open(public_verification_key, "rb") as f3:
                files = {
                    "original_file": (
                        os.path.basename(original_file),
                        f1,
                        "application/octet-stream",
                    ),
                    "signature_file": (
                        os.path.basename(file_path),
                        f2,
                        "application/octet-stream",
                    ),
                    "public_verification_key": (
                        os.path.basename(public_verification_key),
                        f3,
                        "application/octet-stream",
                    ),
                }
                data = {
                    "algo_id": algo_id,
                    "file_id": file_id
                }
                click.echo(f"Sending file '{os.path.basename(file_path)}' to API at {endpoint} using algo_id={algo_id}...")
                response = requests.post(endpoint, files=files, data=data)

                if response.status_code != 200:
                    click.echo(f"API error: {response.text}")
                    return False, f"API error: {response.text}", {}

                if "application/octet-stream" in response.headers.get("Content-Type", ""):
                    if save_path and os.path.isdir(save_path):
                        output_file = os.path.join(save_path, "verified_" + (os.path.basename(original_file) if original_file else os.path.basename(file_path)))
                    else:
                        output_file = save_path

                    with open(output_file, "wb") as out_f:
                        out_f.write(response.content)
                    message = f"File verified successfully and saved to '{output_file}'"
                    return True, message, {}

                else:
                    click.echo(f"Unexpected response: {response.text}")
                    return False, "Unexpected response from API", {}

        else:
            with open(file_path, "rb") as f2, open(public_verification_key, "rb") as f3:
                files = {
                    "signature_file": (
                        os.path.basename(file_path),
                        f2,
                        "application/octet-stream",
                    ),
                    "public_verification_key": (
                        os.path.basename(public_verification_key),
                        f3,
                        "application/octet-stream",
                    ),
                }
                data = {
                    "algo_id": algo_id,
                    "file_id": file_id
                }
                click.echo(f"Sending file '{os.path.basename(file_path)}' to API at {endpoint} using algo_id={algo_id}...")
                response = requests.post(endpoint, files=files, data=data)

                if response.status_code != 200:
                    click.echo(f"API error: {response.text}")
                    return False, f"API error: {response.text}", {}

                if "application/octet-stream" in response.headers.get("Content-Type", ""):
                    if save_path and os.path.isdir(save_path):
                        output_file = os.path.join(save_path, "verified_" + os.path.basename(file_path))
                    else:
                        output_file = save_path

                    with open(output_file, "wb") as out_f:
                        out_f.write(response.content)
                    message = f"File verified successfully and saved to '{output_file}'"
                    return True, message, {}

                else:
                    click.echo(f"Unexpected response: {response.text}")
                    return False, "Unexpected response from API", {}

    except Exception as e:
        click.echo(f"Exception: {e}")
        return False, f"An unexpected error occurred during file processing: {e}", {}

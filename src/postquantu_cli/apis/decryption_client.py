# src/postquantu_cli/apis/file_encryption.py

import requests
import os
import json
import click

BASE_API_URL = "https://algo.quantumize.dev"


def decryption_file_client(file_path: str, private_decryption_key: str, algo_id: str, save_path: str = None):
    """ 
    Calls the PQC API to decrypt a file using the specified algorithm.

    Args:
        file_path (str): The path to the file to be decrypted.
        algo_id (str): The ID of the algorithm to use (e.g., '1' for NTRU, '2' for KYBER, '3' for SABER).

    Returns:
        tuple: (bool, str, dict) - True if successful, False otherwise; a message; and API response data.
    """
    if not os.path.exists(file_path):
        return False, f"File not found: '{file_path}'", {}

    if not os.path.isfile(file_path):
        return False, f"Path is not a file: '{file_path}'", {}

    if private_decryption_key is None or not os.path.isfile(private_decryption_key):
        return False, f"Private decryption key file not found: '{private_decryption_key}'", {}
    
    endpoint = f"{BASE_API_URL}/decryption/"

    try:
        with open(file_path, "rb") as f, open(private_decryption_key, "rb") as key_f:
            files = {
                "encrypted_file": (
                    os.path.basename(file_path),
                    f,
                    "application/octet-stream",
                ),
                "private_decryption_key": (
                    os.path.basename(private_decryption_key),
                    key_f,
                    "application/octet-stream",
                )   
            }
     
            data = {"algo_id": algo_id}

            click.echo(
                f"Sending file '{os.path.basename(file_path)}' to API  using algo_id={algo_id}..."
            )
            response = requests.post(endpoint, files=files, data=data)

            if response.status_code != 200:
                click.echo(f"API error: {response.text}")
                return False, f"API error: {response.text}", {}

            if "application/octet-stream" in response.headers.get("Content-Type", ""):
                if os.path.isdir(save_path):
                    output_file = os.path.join(save_path, "decrypted_" + os.path.basename(file_path).replace(".PEM", ".txt"))
                else:
                    output_file = save_path

                with open(output_file, "wb") as out_f:
                    out_f.write(response.content)
                message = f"File decrypted successfully and saved to '{output_file}'"
                return True, message, {}

            else:
                click.echo(f"Unexpected response: {response.text}")
                return False, "Unexpected response from API", {}

    except Exception as e:
        click.echo(f"Exception: {e}")
        return False, f"An unexpected error occurred during file processing: {e}", {}

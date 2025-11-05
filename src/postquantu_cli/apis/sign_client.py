import requests
import os
import json
import click

BASE_API_URL = "https://algo.quantumize.dev"


def sign_file_client(file_path: str, algo_id: str, file_id: str = None, save_original_file: bool = True):
    """
    Calls the PQC API to sign a file using the specified algorithm.

    Args:
        file_path (str): The path to the file to be signed. # <-- Cambiado a 'signed'
        algo_id (str): The ID of the algorithm to use (e.g., '1' for Dilithium, '2' for FALCON, '3' for SPHINCS).
        file_id (str, optional): An ID for the file, often used by the API for naming.
                                 If None, uses the base filename.

    Returns:
        tuple: (bool, str, dict) - True if successful, False otherwise; a message; and API response data.
    """

    if not os.path.exists(file_path):
        return False, f"File not found:'{file_path}'", {}

    if not os.path.isfile(file_path):
        return False, f"Path is not a file: '{file_path}'", {}

    if file_id is None:
        file_id = os.path.basename(file_path).split(".")[0]

    endpoint = f"{BASE_API_URL}/signing/"

    try:
        with open(file_path, "rb") as f:
            files = {
                "file_to_sign": (
                    os.path.basename(file_path),
                    f,
                    "application/octet-stream",
                )
            }
            data = {""
            "file_id": file_id, 
            "algo_id": algo_id,
            "save_original_file": str(save_original_file).lower()
            }

            click.echo(
                f"Sending file '{os.path.basename(file_path)}' with ID '{file_id}' to API at {endpoint} using algo_id={algo_id}..."
            )

            response = requests.post(endpoint, files=files, data=data)

            if response.status_code == 200:
                response_data = response.json()
                message = response_data.get("message", "File signed successfully.")
                #key_name = response_data.get("key_name", "N/A")
                #signed_file_name = response_data.get("signed_file_name", "N/A")
                full_message = [
                    f"{message}\n",
                    f"   signature_file_name: {response_data.get('signature_file_name')}\n"
                    f"   signature_file_hash: {response_data.get('signature_file_hash')}\n"
                    f"   public_verification_key_name: {response_data.get('public_verification_key_name')}\n"
                    f"   public_verification_key_hash: {response_data.get('public_verification_key_hash')}\n"
                    #f"   original_file_name: {response_data.get('original_file_name')}\n"
                ]

                full_message = "\n".join(full_message)
                return True, full_message, response_data
            else:
                error_detail = response.text
                try:
                    error_json = response.json()
                    if "detail" in error_json:
                        error_detail = error_json["detail"]
                except json.JSONDecodeError:
                    pass
                return False, f"API Error {response.status_code}: {error_detail}", {}

    except requests.exceptions.ConnectionError:
        return (
            False,
            f"Connection error: Could not connect to API at {BASE_API_URL}. Is your API server running?",
            {},
        )
    except requests.exceptions.Timeout:
        return (
            False,
            "Request to API timed out. The server might be slow or unresponsive.",
            {},
        )
    except requests.exceptions.RequestException as e:
        return False, f"An error occurred during the API request: {e}", {}
    except Exception as e:
        return False, f"An unexpected error occurred during file processing: {e}", {}

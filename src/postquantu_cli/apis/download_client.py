import requests
import os


BASE_API_URL = "https://algo.quantumize.dev"

def download_encrypted_file(file_path: str, save_dir: str):

    endpoint = f"{BASE_API_URL}/download_file/"

    params = {
        "file_path": file_path,
        "file_name": file_path
    }

    response = requests.post(endpoint, params=params, stream=True)
    if response.status_code == 200:
        output_file = os.path.join(save_dir, os.path.basename(file_path))
        with open(output_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return True, f"File downloaded and saved as '{output_file}'"
    else:
        return False, f"Download failed: {response.text}"
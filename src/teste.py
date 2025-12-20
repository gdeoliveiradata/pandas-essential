import requests
import zipfile

def download_dataset(api_url, zip_path, raw_folder):
    # Get the binary data from the API
    with requests.get(api_url, stream=True) as r:
        
        # Raise an error if it occurs
        r.raise_for_status()

        # Write the binary data to a .zip file
        with open(zip_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    with zipfile.ZipFile(zip_path, "r") as zip:
        zip.extractall(path=raw_folder)

    print(f"CSV downloaded and saved to {raw_folder}.")


api_url = "https://www.kaggle.com/api/v1/datasets/download/fatihilhan/global-superstore-dataset"
zip_path = "./data/landing/global-superstore-dataset.zip"
raw_folder = "./data/raw/"

download_dataset(api_url, zip_path, raw_folder)

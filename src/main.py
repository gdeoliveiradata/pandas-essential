import os
import requests
import zipfile
import numpy as np
import pandas as pd

def download_dataset(api_url, zip_path, raw_folder):
    # Check if the file already exists
    if os.path.exists(zip_path):
        print(f"CSV already downloaded and saved to {raw_folder}.")
        return

    # Get the dataset from the API
    with requests.get(api_url, stream=True) as r:
        
        # Raise an exception for bad status codes
        r.raise_for_status()

        # Write the binary data in chunks to a .zip file
        with open(zip_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    # Extract the .csv file to the raw folder
    with zipfile.ZipFile(zip_path, "r") as zip:
        zip.extractall(path=raw_folder)

    print(f"CSV downloaded and saved to {raw_folder}.")


api_url = "https://www.kaggle.com/api/v1/datasets/download/fatihilhan/global-superstore-dataset"
zip_path = "./data/landing/global-superstore-dataset.zip"
raw_folder = "./data/raw/"

download_dataset(api_url, zip_path, raw_folder)

df = pd.read_csv("./data/raw/superstore.csv")

print(df.describe())

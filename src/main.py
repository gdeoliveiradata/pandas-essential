import requests

def download_dataset(url, save_path):
    # Send a GET to the API, streaming the response
    response = requests.get(url, stream=True)

    # Raise exception if the request was unsuccessful
    response.raise_for_status()

    # Open the file in binary write mode ('wb')
    with open(save_path, 'wb') as f:
        # Write the content in chunks
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Dataset downloaded and saved to {save_path}.")

dt_url = "https://www.kaggle.com/api/v1/datasets/download/fatihilhan/global-superstore-dataset"

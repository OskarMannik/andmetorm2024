import os
import requests


def download_files(urls, save_folder):
    """
    Downloads JSON files from list of urls.

    Args:
        urls ([string]): List of urls.
        save_folder (string): Path where to save the files.
    """
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an error for HTTP errors

            # Extract the filename from the URL
            file_name = url.split("/")[-1]
            file_path = os.path.join(save_folder, file_name+".json")

            # Write the content to a file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(response.text)

            print(f"Downloaded and saved: {file_name}")

        except requests.exceptions.RequestException as e:
            print(f"Failed to download {url}: {e}")
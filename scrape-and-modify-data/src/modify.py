import csv
import os
import json

def json_to_csv(json_file, save_folder):
    """
    Converts JSON file to CSV file.

    Args:
        json_file (string): Path to JSON file.
        save_folder (string): Path where to save the CSV file.
    """

    # Check if the save folder exists
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    try:
        # Open the JSON file
        with open(json_file, mode='r', encoding='utf-8') as file:
            # Load the JSON data
            json_data = json.load(file)

        # Extract the filename from the URL
        file_name = json_file.split("/")[-1]
        file_name = file_name.split(".")[0]
        file_path = os.path.join(save_folder, file_name + ".csv")

        # Open the output CSV file
        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            # Create a CSV writer object
            writer = csv.DictWriter(csvfile, fieldnames=json_data[0].keys())

            # Write the header row
            writer.writeheader()

            # Write the data rows
            writer.writerows(json_data)

            print(f"Saved: {file_name}")


    except Exception as e:
        print(f"An unexpected error occurred: {e}")
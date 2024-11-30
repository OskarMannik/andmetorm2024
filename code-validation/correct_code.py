import os
from dotenv import load_dotenv
import google.generativeai as genai


def code_correction(file_path, error, csv_path):
    # Load the environment variables
    load_dotenv()

    # Get the API key from the environment variables
    api_key = os.getenv("GOOGLE_API_KEY")

    # Read the content of the CSV file
    with open(file_path, "r") as file:
        file_content = file.read()


    system_prompt = f"Sa oled programmeerija, kes kirjutab CSV andmete visualiseerimis koodi, mis on vigane. Sinu ülesanne on parandada: {error} viga koodis ning tagastada parandatud kood."

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")
    response_text = model.generate_content([
        system_prompt,
        file_content,
    ]).text

    # Write the corrected code to a new file
    with open(file_path, "w") as file:
        file.write(response_text)



import os
from dotenv import load_dotenv
import google.generativeai as genai

class Translator:
    """
    A class to handle translation between Estonian and English using Google's Generative AI Pro model.
    """

    def __init__(self):
        """
        Initialize the TranslatorPro class by configuring the API key and setting the model.
        """
        # Load API key from .env file
        load_dotenv()
        self.api_key = os.getenv("GOOGLE_API")
        if not self.api_key:
            raise ValueError("API key is not set. Please configure GOOGLE_API in your .env file.")
        
        # Configure Generative AI
        genai.configure(api_key=self.api_key)

        # Initialize the model directly (to match the working example)
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def translate_est_to_eng(self, estonian_text):
        """
        Translate Estonian text to English using the Pro model.
        """
        prompt = f"""
        Translate the following Estonian text to English:
        {estonian_text}
        """
        # Generate content using the Pro model
        response = self.model.generate_content(prompt)
        return response.text.strip()

    def translate_eng_to_est(self, english_text):
        """
        Translate English text to Estonian using the Pro model.
        """
        prompt = f"""
        Translate the following English text to Estonian:
        {english_text}
        """
        # Generate content using the Pro model
        response = self.model.generate_content(prompt)
        return response.text.strip()

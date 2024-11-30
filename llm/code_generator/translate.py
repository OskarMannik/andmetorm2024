
'''
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
'''
import os
from dotenv import load_dotenv
from groq import Groq

class Translator:
    """
    A class to handle translation between Estonian and English using the Llama70B model via the Groq client.
    """

    def __init__(self):
        """Initialize the Translator class by configuring the Groq client and setting the model."""
        # Load API key from .env file
        load_dotenv()
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("API key is not set. Please configure GROQ_API_KEY in your .env file.")

        # Configure Groq client
        self.client = Groq(api_key=self.api_key)

        # Set the model name (use 'llama70b' or the appropriate model identifier)
        self.model_name = os.getenv("GROQ_MODEL_NAME", "llama-3.1-70b-versatile")  # Default to llama-2-70b-chat-4k if not set

    def _get_chatbot_response(self, messages, temperature=0.2):
        """Private method to get response from the Groq client."""
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=1000,
        )
        return response.choices[0].message.content.strip()

    def translate_est_to_eng(self, estonian_text):
        """Translate Estonian text to English using the Llama70B model."""
        prompt = f"Translate the following Estonian text to English:\n\n{estonian_text}\n\nTranslation:"
        messages = [{"role": "user", "content": prompt}]
        translation = self._get_chatbot_response(messages)
        return translation

    def translate_eng_to_est(self, english_text):
        """Translate English text to Estonian using the Llama70B model."""
        prompt = f"Translate the following English text to Estonian:\n\n{english_text}\n\nTranslation:"
        messages = [{"role": "user", "content": prompt}]
        translation = self._get_chatbot_response(messages)
        return translation

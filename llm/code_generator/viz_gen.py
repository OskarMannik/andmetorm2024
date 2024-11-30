import os
from groq import Groq
import pandas as pd
from dotenv import load_dotenv
from .translate import Translator
from .code_corrector import ReviewerAgent  # Assuming ReviewerAgent is implemented in reviewer.py
import re
import matplotlib.pyplot as plt
import numpy as np


class VisualizationGenerator:
    """
    A class to generate, review, and iteratively refine visualization code based on user input and feedback.
    """

    def __init__(self):
        """Initialize the VisualizationGenerator with Groq client, Translator, and ReviewerAgent"""
        load_dotenv()
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
        )
        self.model_name = os.getenv("GROQ_MODEL_NAME", "mixtral-8x7b-32768")
        self.translator = Translator()
        self.reviewer = ReviewerAgent(client=self.client)
        self.data = None

    def _get_chatbot_response(self, messages, temperature=0.2):
        """Private method to get response from Groq"""
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=2000,
        )
        return response.choices[0].message.content

    def generate_visualization_code(self, data_columns, sample_row, csv_filename, user_requirements, data_description=None):
        """Generate visualization code based on user input and data analysis"""
        column_types = [f"{col}: {type(val).__name__}" for col, val in zip(data_columns, sample_row)]
        user_requirements_english = self.translator.translate_est_to_eng(user_requirements)

        prompt = f"""Given the following dataset information:
Columns and data types: {column_types}
Sample row of data: {dict(zip(data_columns, sample_row))}
CSV filename: {csv_filename}
{f'Additional context about the data: {data_description}' if data_description else ''}
User requirements: {user_requirements_english}

Generate Python code that creates a clear and professional visualization using matplotlib. Please:
1. Import only pandas, matplotlib.pyplot, and numpy
2. Include detailed comments explaining each step
3. Use the user's requirements to determine the appropriate chart type and data to visualize
4. Save the visualization as 'output_visualization.png'
5. End with plt.show()

Provide only the Python code with comments."""

        messages = [{'role': 'user', 'content': prompt}]
        code = self._get_chatbot_response(messages, temperature=0.2)
        return code

    def clean_generated_code(self, code):
        """Clean the generated Python code by removing unintended artifacts."""
        cleaned_code = re.sub(r"^\s*['\"`]{3}.*?\n", "", code, flags=re.DOTALL)  # Remove opening triple quotes
        cleaned_code = re.sub(r"['\"`]{3}\s*$", "", cleaned_code)  # Remove closing triple quotes
        return cleaned_code.strip()

    def save_and_execute_code(self, code, file_path):
        """Save the cleaned Python code to a file and execute it."""
        try:
            # Clean the code
            cleaned_code = self.clean_generated_code(code)

            # Save the cleaned code to a file
            with open(file_path, "w") as f:
                f.write(cleaned_code)
            print(f"Code saved to {file_path}")

            # Execute the cleaned code
            exec_globals = {}
            exec(cleaned_code, exec_globals)
            print("Visualization successfully generated and saved as PNG!")
        except Exception as e:
            raise Exception(f"Error executing the visualization code: {e}")

    def generate_visualization_from_csv(self, csv_path, data_description, user_prompt):
        # Load the data
        self.data = pd.read_csv(csv_path)
        
        # Basic visualization based on user prompt
        # You can expand this to handle different types of visualizations
        if 'histogram' in user_prompt.lower():
            self._create_histogram()
        elif 'line' in user_prompt.lower():
            self._create_line_plot()
        else:
            # Default to histogram
            self._create_histogram()
        
        return True

    def _create_histogram(self):
        plt.figure(figsize=(10, 6))
        plt.hist(self.data['aastakokku'].dropna(), bins=30, edgecolor='black')
        plt.title('Distribution of Total Stock of Fish in a Year')
        plt.xlabel('Total Stock of Fish')
        plt.ylabel('Frequency')
        plt.grid(True)

    def _create_line_plot(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.data['aastakokku'].dropna())
        plt.title('Total Stock of Fish Over Time')
        plt.xlabel('Index')
        plt.ylabel('Total Stock of Fish')
        plt.grid(True)

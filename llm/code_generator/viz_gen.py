import os
import re
from groq import Groq
import pandas as pd
from dotenv import load_dotenv
from .translate import Translator
from .code_corrector import ReviewerAgent  # Assuming ReviewerAgent is implemented in reviewer.py


class VisualizationGenerator:
    """
    A class to generate, review, and execute visualization code based on user input and feedback.
    """

    def __init__(self):
        """Initialize the VisualizationGenerator with Groq client, Translator, and ReviewerAgent"""
        load_dotenv()
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
        )
        self.model_name = os.getenv("GROQ_MODEL_NAME", "llama-3.1-70b-versatile")
        self.translator = Translator()
        self.reviewer = ReviewerAgent(client=self.client)
        self.working_code = None  # Store the current working code
        self.df = None  # Store the DataFrame

    def _get_chatbot_response(self, messages, temperature=0.2):
        """Private method to get response from Groq"""
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=2000,
        )
        return response.choices[0].message.content

    def generate_visualization_code(self, csv_path, user_requirements, data_description=None):
        """
        Generate visualization code based on user input and data analysis.
        Returns the generated code as a string.
        """
        # Read the CSV file if not already loaded
        if self.df is None:
            self.df = pd.read_csv(csv_path)

        data_columns = self.df.columns.tolist()
        sample_row = self.df.iloc[0].tolist()
        column_types = [f"{col}: {type(val).__name__}" for col, val in zip(data_columns, sample_row)]
        user_requirements_english = self.translator.translate_est_to_eng(user_requirements)

        prompt = f"""Given the following dataset information:
Columns and data types: {column_types}
Sample row of data: {dict(zip(data_columns, sample_row))}
CSV filename: '{csv_path}'
{f'Additional context about the data: {data_description}' if data_description else ''}
User requirements: {user_requirements_english}

Generate Python code that creates a clear and professional visualization using matplotlib. Please:
1. Import only pandas, matplotlib.pyplot, and numpy
2. Include detailed comments explaining each step
3. Use the user's requirements to determine the appropriate chart type and data to visualize
4. Save the visualization as 'output_visualization.png' in the 'static' folder
5. Do not call plt.show(); instead, just save the figure

Provide only the Python code with comments."""

        messages = [{'role': 'user', 'content': prompt}]
        code = self._get_chatbot_response(messages, temperature=0.2)
        self.working_code = code  # Store the code for potential future use
        return code

    def clean_generated_code(self, code):
        """Clean the generated Python code by removing unintended artifacts."""
        cleaned_code = re.sub(r"^\s*['\"`]{3}.*?\n", "", code, flags=re.DOTALL)  # Remove opening triple quotes
        cleaned_code = re.sub(r"['\"`]{3}\s*$", "", cleaned_code)  # Remove closing triple quotes
        return cleaned_code.strip()

    def save_and_execute_code(self, code, output_image_path):
        """
        Save the cleaned Python code to a file and execute it.
        The visualization image will be saved to 'output_image_path'.
        """
        try:
            # Clean the code
            cleaned_code = self.clean_generated_code(code)

            # Ensure the output directory exists
            os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

            # Save the cleaned code to a temporary file
            temp_code_file = "temp_visualization_code.py"
            with open(temp_code_file, "w") as f:
                f.write(cleaned_code)

            # Execute the cleaned code with proper context
            exec_globals = {'__name__': '__main__'}
            exec(cleaned_code, exec_globals)
            print(f"Visualization successfully generated and saved at '{output_image_path}'!")

            # Remove the temporary code file
            os.remove(temp_code_file)

        except Exception as e:
            raise Exception(f"Error executing the visualization code: {e}")

    def regenerate_visualization_code(self, csv_path, user_requirements, data_description=None):
        """
        Regenerate the visualization code based on new user requirements.
        Overwrites the previous code and image.
        """
        # Generate new code with updated requirements
        new_code = self.generate_visualization_code(
            csv_path=csv_path,
            user_requirements=user_requirements,
            data_description=data_description
        )
        return new_code

    def review_and_correct_code(self, code, csv_path):
        """
        Review and correct the generated code using ReviewerAgent.
        Returns the corrected code as a string.
        """
        try:
            reviewed_code = self.reviewer.review_and_correct_code(code, csv_path)
            self.working_code = reviewed_code  # Update the working code
            return reviewed_code
        except RuntimeError as review_error:
            raise Exception(f"Error during code review: {review_error}")

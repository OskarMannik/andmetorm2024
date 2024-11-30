import os
from groq import Groq
import pandas as pd
from dotenv import load_dotenv
from .translate import Translator
from .code_corrector import ReviewerAgent  # Assuming ReviewerAgent is implemented in reviewer.py
import re


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

    def generate_visualization_from_csv(self, csv_path, data_description=None):
        """
        Generate, review, and execute visualization code by interacting with the user.
        Allow iterative updates based on user feedback.
        """
        try:
            # Read the CSV file
            df = pd.read_csv(csv_path)
            print("Siin on teie andmete esimesed read:")
            print(df.head())
            print("\nVeergude nimed ja andmetüübid:")
            print(df.dtypes)

            user_requirements = input("\nPalun kirjeldage, millist visualiseerimist soovite luua: ")
            working_code = None  # Store the working code for iterative updates

            while True:
                # Generate the initial or updated visualization code
                if working_code:
                    print("\nUsing the previous working code as a base for updates...")
                generated_code = self.generate_visualization_code(
                    data_columns=df.columns.tolist(),
                    sample_row=df.iloc[0].tolist(),
                    csv_filename=csv_path,
                    user_requirements=user_requirements,
                    data_description=data_description
                )

                print("\nLoodud visualiseerimiskood:\n")
                print(generated_code)

                # Validate and correct code if execution fails
                try:
                    print("\nKontrollime loodud koodi...")
                    reviewed_code = self.reviewer.review_and_correct_code(generated_code, csv_path)
                    print("\nParandatud visualiseerimiskood:\n")
                    print(reviewed_code)
                    working_code = reviewed_code
                except RuntimeError as review_error:
                    print(f"Koodi läbivaatamisel ilmnes viga: {review_error}")
                    return

                # Save and execute the reviewed code
                output_file = "generated_visualization.py"
                self.save_and_execute_code(working_code, output_file)

                # Ask the user if they are satisfied
                satisfaction = input("\nKas olete loodud visualiseerimiskoodiga rahul? (jah/ei): ").strip().lower()
                if satisfaction in ['jah', 'j']:
                    print("Visualization finalized and saved successfully.")
                    break
                else:
                    print("\nPalun täpsustage, mida soovite visualiseeringus muuta.")
                    user_requirements = input("Uued nõuded: ")

        except Exception as e:
            raise Exception(f"CSV faili lugemisel tekkis viga: {str(e)}")

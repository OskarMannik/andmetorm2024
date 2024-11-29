from groq import Groq
import ast
from dotenv import load_dotenv
import os
import pandas as pd

class ReviewerAgent:
    def __init__(self):
        """Initialize the ReviewerAgent with Groq client and model settings"""
        load_dotenv()
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
        )
        self.model_name = os.getenv("GROQ_MODEL_NAME", "mixtral-8x7b-32768")

    def _get_review_response(self, messages, temperature=0.2):
        """Get response from Groq"""
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=2000,
        )
        return response.choices[0].message.content

    def _analyze_csv_data(self, csv_path):
        """Analyze CSV data for potential issues"""
        try:
            # Read a small sample of the data
            sample_df = pd.read_csv(csv_path, nrows=5)
            
            # Check for common issues
            issues = []
            for column in sample_df.columns:
                # Check for comma-separated numbers
                if sample_df[column].dtype == 'object':
                    sample_val = str(sample_df[column].iloc[0])
                    if ',' in sample_val and any(c.isdigit() for c in sample_val):
                        issues.append(f"Column '{column}' contains comma-separated numbers")
            
            return issues
        except Exception as e:
            return [f"Error analyzing CSV: {str(e)}"]

    def validate_python_syntax(self, code):
        """Check if the code has valid Python syntax"""
        try:
            ast.parse(code)
            return True
        except SyntaxError as e:
            return False, str(e)

    def review_and_correct_code(self, generated_code, csv_path):
        """Review and correct the generated visualization code"""
        # Analyze CSV for potential issues
        data_issues = self._analyze_csv_data(csv_path)
        
        prompt = f"""Review and correct this Python visualization code. The CSV file has the following issues to address:
        {', '.join(data_issues)}

        Ensure the code:
        1. Has valid Python syntax
        2. Implements efficient data loading:
           - Uses pd.read_csv with appropriate parameters
           - Uses on_bad_lines='skip' for error handling
        3. Includes proper data type handling:
           - Converts string numbers to appropriate numeric types
           - Handles categorical data correctly
           - Deals with potential missing or invalid values
        4. Includes all necessary imports
        5. Uses best practices for data visualization:
           - Appropriate sampling/aggregation before plotting
           - Clear labels and titles
           - Proper figure sizing and layout
        6. Is properly formatted and commented
        
        Here's the code to review:

        {generated_code}

        Please provide the corrected version of the code that addresses all issues found.
        Return ONLY the corrected Python code, no explanations."""

        messages = [{'role': 'user', 'content': prompt}]
        corrected_code = self._get_review_response(messages)

        # Validate the corrected code
        validation_result = self.validate_python_syntax(corrected_code)
        if isinstance(validation_result, tuple):
            # If validation failed, try to get a fix
            return self._get_syntax_fix(corrected_code, validation_result[1])
        
        return corrected_code

    def _get_syntax_fix(self, code, error):
        """Get a fix for syntax errors"""
        prompt = f"""This Python code has a syntax error: {error}
        Please fix the code and return ONLY the corrected version:

        {code}"""

        messages = [{'role': 'user', 'content': prompt}]
        fixed_code = self._get_review_response(messages)
        
        # Validate again
        if self.validate_python_syntax(fixed_code) is True:
            return fixed_code
        else:
            raise ValueError("Unable to generate valid Python code after multiple attempts")
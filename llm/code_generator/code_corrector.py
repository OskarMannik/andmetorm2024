import ast
import re
from collections import defaultdict

class ReviewerAgent:
    """
    A class to review and correct Python visualization code.
    """

    def __init__(self, client):
        """
        Initialize the ReviewerAgent with Groq client.
        """
        self.client = client
        self.retry_limit = 5
        self.error_tracker = defaultdict(int)  # Track error occurrences

    def validate_python_syntax(self, code):
        """
        Validate the Python syntax of the given code.
        """
        try:
            ast.parse(code)
            return True, None  # Return a tuple with True and None for no error
        except SyntaxError as e:
            return False, str(e)  # Return False and the error message

    def clean_code(self, code):
        """
        Clean the generated Python code to remove unintended artifacts such as
        markdown formatting, triple quotes, or other issues.
        """
        cleaned_code = re.sub(r"^\s*['\"`]{3}.*?\n", "", code, flags=re.DOTALL)  # Remove opening triple quotes
        cleaned_code = re.sub(r"['\"`]{3}\s*$", "", cleaned_code)  # Remove closing triple quotes
        return cleaned_code.strip()

    def validate_and_execute_code(self, code, csv_path):
        """
        Validate the code syntax and execute it.
        Capture and return runtime errors, if any.
        """
        # Clean the code before validation
        cleaned_code = self.clean_code(code)

        # Validate syntax
        is_valid, error_message = self.validate_python_syntax(cleaned_code)
        if not is_valid:
            return False, f"Syntax Error: {error_message}"

        # Attempt to execute the code
        try:
            exec_globals = {}
            exec(cleaned_code, {"csv_path": csv_path}, exec_globals)
            return True, None  # Code executed successfully
        except Exception as e:
            return False, f"Runtime Error: {str(e)}"

    def review_and_correct_code(self, code, csv_path):
        """
        Review and correct the Python code.
        Retry fixing errors during execution.
        """
        original_code = code  # Preserve the original code
        syntax_error_count = 0  # Counter for repeated syntax errors

        for attempt in range(self.retry_limit):
            print(f"Review attempt {attempt + 1}...")
            is_valid, error_message = self.validate_and_execute_code(code, csv_path)

            if is_valid:
                print("Code executed successfully!")
                return code

            print(f"Error detected: {error_message}")

            # Detect repeated syntax errors
            if "Syntax Error" in error_message:
                syntax_error_count += 1
                if syntax_error_count >= 2:  # Handle repeated syntax errors
                    print("Repeated syntax error detected. Requesting a complete rewrite.")
                    prompt = f"""The following Python code caused repeated syntax errors during execution:
                    {error_message}

                    Here is the problematic code:
                    {code}

                    Please rewrite the entire code to ensure:
                    - It is valid, executable Python code without syntax errors.
                    - All necessary imports and preprocessing steps are included.
                    - The code runs successfully without any formatting issues or markdown artifacts.

                    Return ONLY the fixed and complete Python code without any explanations:
                    """
                    # Send the rewrite request
                    messages = [{'role': 'user', 'content': prompt}]
                    try:
                        response = self.client.chat.completions.create(
                            model="mixtral-8x7b-32768",
                            messages=messages,
                            temperature=0.2,
                            max_tokens=2000,
                        ).choices[0].message.content
                    except Exception as e:
                        print(f"Error during model response: {e}")
                        break

                    # Sanitize and replace the code with the rewritten output
                    code = self.clean_code(response)
                    syntax_error_count = 0  # Reset the counter after a rewrite
                    continue

            # Handle other errors or refine the prompt
            prompt = f"""The following Python code caused an error during execution:
            {error_message}

            Here is the problematic code:
            {code}

            Please fix the code to resolve the issue and ensure:
            - Syntax errors are corrected.
            - The code runs successfully without errors.
            - The output should ONLY be runnable Python code without any formatting artifacts or markdown syntax.

            Return ONLY the corrected Python code:
            """
            # Send the correction request
            messages = [{'role': 'user', 'content': prompt}]
            try:
                response = self.client.chat.completions.create(
                    model="mixtral-8x7b-32768",
                    messages=messages,
                    temperature=0.2,
                    max_tokens=2000,
                ).choices[0].message.content
            except Exception as e:
                print(f"Error during model response: {e}")
                break

            # Sanitize the returned code
            code = self.clean_code(response)

        # Provide a fallback response if retries are exhausted
        print("Failed to fix and execute the code after multiple attempts.")
        print(f"Returning the last working version or the original code.")
        return original_code



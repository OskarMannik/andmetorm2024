import ast

class ReviewerAgent:
    """
    A class to review and correct Python visualization code.
    """

    def __init__(self, client):
        """
        Initialize the ReviewerAgent with Groq client.
        """
        self.client = client
        self.retry_limit = 3

    def validate_python_syntax(self, code):
        """
        Validate the Python syntax of the given code.
        """
        try:
            ast.parse(code)
            return True, None  # Return a tuple with True and None for no error
        except SyntaxError as e:
            return False, str(e)  # Return False and the error message


    def validate_and_execute_code(self, code, csv_path):
        """
        Validate the code syntax and execute it.
        Capture and return runtime errors, if any.
        """
        # Validate syntax
        is_valid, error_message = self.validate_python_syntax(code)
        if not is_valid:
            return False, f"Syntax Error: {error_message}"

        # Attempt to execute the code
        try:
            exec_globals = {}
            exec(code, {"csv_path": csv_path}, exec_globals)
            return True, None  # Code executed successfully
        except Exception as e:
            return False, f"Runtime Error: {str(e)}"


    def review_and_correct_code(self, code, csv_path):
        """
        Review and correct the Python code.
        Retry fixing errors during execution.
        """
        for attempt in range(self.retry_limit):
            print(f"Review attempt {attempt + 1}...")
            is_valid, error_message = self.validate_and_execute_code(code, csv_path)

            if is_valid:
                print("Code executed successfully!")
                return code

            print(f"Error detected: {error_message}")
            prompt = f"""The following Python code caused an error during execution:
            {error_message}

            Here is the problematic code:
            {code}

            Please fix the code to resolve the issue and return ONLY the corrected Python code:
            """
            # Send the error and code for correction
            messages = [{'role': 'user', 'content': prompt}]
            code = self.client.chat.completions.create(
                model="mixtral-8x7b-32768",
                messages=messages,
                temperature=0.2,
                max_tokens=2000,
            ).choices[0].message.content

        # If retries are exhausted, raise an error
        raise RuntimeError("Failed to fix and execute the code after multiple attempts.")

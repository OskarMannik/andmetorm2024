from validate_syntax import validate_syntax

def test_code(file_path):
    """
    Test the code in the given file.

    Parameters:
    file_path (str): The path to the file containing the code.

    Returns:
    bool: True if the code runs without errors, False otherwise.
    str: The error message if the code has errors, None otherwise.
    """

    syntax_valid, error_message = validate_syntax(file_path)

    if not syntax_valid:
        return False, error_message

    with open(file_path, 'r') as file:
        code = file.read()

    try:
        exec(code)
        return True, None
    except Exception as e:
        return False, str(e)
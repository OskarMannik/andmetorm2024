import ast


def validate_syntax(path_to_file):
    """
    Validate the syntax of the given code.

    Parameters:
    path_to_file (str): The path to the file containing the code.

    Returns:
    bool: True if the syntax is valid, False otherwise.
    str: The error message if the syntax is invalid, None otherwise.
    """

    with open(path_to_file, 'r') as file:
        code = file.read()

    try:
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, str(e)
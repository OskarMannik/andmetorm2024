import os


"""
1) Make .py file
2) Read string line by line
3) Write each line to .py file
"""

py_string = "print('Hello World!')"
py_file_save_path = "./data"



def txt_to_py_file(py_string, py_file_save_path):

    # make a py file path
    py_file_path = os.path.join(py_file_save_path, 'chart_generation.py')

    # make a .py file
    with open(py_file_path, 'w') as f:
        f.write(py_string)
        print(f"File saved at {py_file_path}")



txt_to_py_file(py_string, py_file_save_path)
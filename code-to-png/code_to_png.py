import os

def code_to_png(code_path, png_path):

    # make a png file path
    # png_file_path = os.path.join(png_path, 'chart.png')

    # run py file
    os.system(f'python {code_path}')

    # make or update png path



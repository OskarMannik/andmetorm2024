from flask import Flask, request, send_file
from io import BytesIO
from ..visualization_generator import visualization_generator
# Add the current directory to the Python path to ensure visualization_generator can be imported

app = Flask(_name_)

@app.route('/generate-image', methods=['POST'])
def generate_image():
    input_string = request.json.get('input')  # Receive input string
    # Generate the image from the input string (e.g., via some image generation library)

    visualization_generator.generate_visualization()

    img_path = "/llm/output_visualization.png"

    # Load the image from the file
    with open(img_path, 'rb') as img_file:
        img_data = img_file.read()

    # Save the image to a BytesIO object
    img_io = BytesIO(img_data)
    img_io.seek(0)

    # Return the image as a response
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='output.png')

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
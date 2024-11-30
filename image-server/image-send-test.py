from flask import Flask, request, send_file
from flask_cors import CORS
from io import BytesIO
from PIL import Image

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/send-image', methods=['POST'])
def send_image():
    # Get the JSON body from the request
    # post_body = request.get_json()  # If the body is JSON
    # Alternatively, use `request.data` for raw body or `request.form` for form data

    # print("Received POST body:", post_body)

    # Example: Generate a simple PNG image dynamically
    img = Image.new('RGB', (100, 100), color=(255, 0, 0))  # Red square

    # load image "output_visualization.png"
    # img = Image.open("./output_visualization.png")

    # Save the image to a BytesIO object
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)  # Go to the start of the BytesIO object

    # Send the image as a response
    return send_file(img_io, mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

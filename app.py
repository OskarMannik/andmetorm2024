from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from llm.code_generator import VisualizationGenerator
import matplotlib
matplotlib.use('Agg')
import os
import matplotlib.pyplot as plt

app = Flask(__name__)
CORS(app)

viz_gen = VisualizationGenerator()

# Define the path for saving images
SAVE_PATH = "./frontend/public/data/"
os.makedirs(SAVE_PATH, exist_ok=True)

@app.route('/generate-visualization', methods=['POST'])
def generate_visualization():
    try:
        data = request.json
        user_message = data.get('message')
        data_description = data.get('data_description')

        # Generate visualization
        visualization_result = viz_gen.generate_visualization_from_csv(
            csv_path="./llm/data.csv",
            data_description=data_description,
            user_prompt=user_message
        )

        # Generate unique filename
        filename = f"visualization_{hash(user_message)}.png"
        save_path = os.path.join(SAVE_PATH, filename)

        # Save the plot to the specified location
        plt.savefig(save_path)
        plt.close()  # Close the plot to free memory

        return jsonify({
            'success': True,
            'response': 'Visualization generated successfully!',
            'visualization': f"/data/{filename}"
        })

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e),
            'response': 'Error generating visualization'
        }), 500

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)

from flask import Flask, render_template, request, redirect, url_for
from code_generator import VisualizationGenerator
import os

app = Flask(__name__)

# Ensure the 'static' directory exists for storing images
os.makedirs('static', exist_ok=True)

# Global variables to maintain state
viz_gen = VisualizationGenerator()
csv_path = "../scrape-and-modify-data/output/t_awtabel002_02_curr.csv"
data_description = "Vee andmestik"  # Optional data description in Estonian
output_image_path = "static/output_visualization.png"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user requirements from the form
        user_requirements = request.form.get('user_requirements', '').strip()
        
        if not user_requirements:
            error = "Palun sisestage oma visualiseerimise nõuded."
            return render_template('index.html', error=error)
        
        try:
            # Generate initial visualization
            generate_initial_visualization(
                csv_path=csv_path,
                data_description=data_description,
                user_requirements=user_requirements,
                output_image_path=output_image_path
            )
            # Redirect to the visualization page
            return redirect(url_for('visualization'))
        
        except Exception as e:
            error = f"Visualiseerimise genereerimisel tekkis viga: {str(e)}"
            return render_template('index.html', error=error)
    
    return render_template('index.html')

@app.route('/visualization', methods=['GET', 'POST'])
def visualization():
    if request.method == 'POST':
        # Check if the user is satisfied
        user_satisfied = request.form.get('user_satisfied')
        
        if user_satisfied == 'yes':
            # User is satisfied, end the process
            message = "Võid faili kasutada!"
            return render_template('visualization.html', image_url='/' + output_image_path, message=message)
        else:
            # User is not satisfied, ask for new requirements
            return redirect(url_for('update_visualization'))
    
    return render_template('visualization.html', image_url='/' + output_image_path)

@app.route('/update_visualization', methods=['GET', 'POST'])
def update_visualization():
    if request.method == 'POST':
        # Get the new user requirements from the form
        new_user_requirements = request.form.get('new_user_requirements', '').strip()
        
        if not new_user_requirements:
            error = "Palun sisestage uued visualiseerimise nõuded."
            return render_template('update_visualization.html', error=error)
        
        try:
            # Regenerate visualization with new requirements
            regenerate_visualization(
                csv_path=csv_path,
                data_description=data_description,
                new_user_requirements=new_user_requirements,
                output_image_path=output_image_path
            )
            # Redirect back to the visualization page
            return redirect(url_for('visualization'))
        
        except Exception as e:
            error = f"Visualiseeringu uuendamisel tekkis viga: {str(e)}"
            return render_template('update_visualization.html', error=error)
    
    return render_template('update_visualization.html')

def generate_initial_visualization(csv_path, data_description, user_requirements, output_image_path):
    """
    Generates the initial visualization based on the user's requirements.
    """
    try:
        print("Generating initial visualization code...")
        
        # Generate the visualization code
        generated_code = viz_gen.generate_visualization_code(
            csv_path=csv_path,
            user_requirements=user_requirements,
            data_description=data_description
        )
        
        # Review and correct the code
        corrected_code = viz_gen.review_and_correct_code(
            code=generated_code,
            csv_path=csv_path
        )
        
        # Save and execute the corrected code to generate the visualization image
        viz_gen.save_and_execute_code(
            code=corrected_code,
            output_image_path=output_image_path
        )
        
        print("Initial visualization generated successfully!")
        print(f"Visualization image saved at: {output_image_path}")
        
    except Exception as e:
        print(f"Error in generating initial visualization: {str(e)}")
        raise  # Re-raise exception for further handling if needed

def regenerate_visualization(csv_path, data_description, new_user_requirements, output_image_path):
    """
    Regenerates the visualization based on updated user requirements.
    Overwrites the previous visualization image.
    """
    try:
        print("Regenerating visualization code with new requirements...")
        
        # Regenerate the visualization code with updated requirements
        new_generated_code = viz_gen.regenerate_visualization_code(
            csv_path=csv_path,
            user_requirements=new_user_requirements,
            data_description=data_description
        )
        
        # Review and correct the new code
        new_corrected_code = viz_gen.review_and_correct_code(
            code=new_generated_code,
            csv_path=csv_path
        )
        
        # Save and execute the new corrected code to generate the updated visualization image
        viz_gen.save_and_execute_code(
            code=new_corrected_code,
            output_image_path=output_image_path
        )
        
        print("Visualization regenerated successfully!")
        print(f"Visualization image updated at: {output_image_path}")
        
    except Exception as e:
        print(f"Error in regenerating visualization: {str(e)}")
        raise  # Re-raise exception for further handling if needed

if __name__ == '__main__':
    app.run(debug=True)

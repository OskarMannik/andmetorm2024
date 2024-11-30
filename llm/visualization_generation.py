from code_generator import VisualizationGenerator

def generate_initial_visualization(csv_path, data_description, user_requirements, output_image_path):
    """
    Generates the initial visualization based on the user's requirements.
    """
    # Initialize the VisualizationGenerator
    viz_gen = VisualizationGenerator()
    
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
    # Initialize the VisualizationGenerator
    viz_gen = VisualizationGenerator()
    
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

def main():
    # Example CSV file path and data description
    csv_path = "../scrape-and-modify-data/output/sademed.csv"
    data_description = "Vee andmestik"  # Optional data description in Estonian
    
    # Initial user requirements in Estonian
    initial_user_requirements = "Soovin näha sademete hulka ajas graafikuna."
    
    # Output image path
    output_image_path = "static/output_visualization.png"  # Ensure 'static' directory exists
    
    try:
        # Generate initial visualization
        generate_initial_visualization(
            csv_path=csv_path,
            data_description=data_description,
            user_requirements=initial_user_requirements,
            output_image_path=output_image_path
        )
        
        # Simulate user satisfaction
        user_satisfied = False  # Hardcoded as 'no' for testing purposes
        
        if not user_satisfied:
            print("\nUser is not satisfied with the initial visualization.")
            # New user requirements (e.g., change line color to red)
            new_user_requirements = "Soovin, et graafiku joon oleks punast värvi."
            print(f"Updating visualization with new requirements: {new_user_requirements}")
            
            # Regenerate visualization with new requirements
            regenerate_visualization(
                csv_path=csv_path,
                data_description=data_description,
                new_user_requirements=new_user_requirements,
                output_image_path=output_image_path
            )
            
    except Exception as e:
        print(f"Error in visualization pipeline: {str(e)}")

if __name__ == "__main__":
    main()

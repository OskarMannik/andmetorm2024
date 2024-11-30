from code_generator import VisualizationGenerator


def main():
    # Initialize the VisualizationGenerator (which includes the ReviewerAgent)
    viz_gen = VisualizationGenerator()
    
    # Example with CSV file
    csv_path = "../scrape-and-modify-data/output/t_awtabel002_02_curr copy.csv"
    description = "Vee andmestik"
    
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
            data_description=description
        )
        
        print("Visualization pipeline completed successfully!")
        
    except Exception as e:
        print(f"Error in visualization pipeline: {str(e)}")

if __name__ == "__main__":
    main()

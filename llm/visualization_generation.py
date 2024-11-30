from code_generator import VisualizationGenerator


def generate_visualization():
    # Initialize the VisualizationGenerator (which includes the ReviewerAgent)
    viz_gen = VisualizationGenerator()

    # Example with CSV file
    csv_path = "./data/data.csv"
    description = "Vee andmestik"
    user_prompt = "line"  # Default to line plot visualization

    try:
        print("Generating initial visualization code...")
        # Generate and process visualization code directly
        viz_gen.generate_visualization_from_csv(
            csv_path=csv_path,
            data_description=description,
            user_prompt=user_prompt
        )

        print("Visualization pipeline completed successfully!")

    except Exception as e:
        print(f"Error in visualization pipeline: {str(e)}")

if __name__ == "__main__":
    main()

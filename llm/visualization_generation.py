from code_generator import VisualizationGenerator


def main():
    # Initialize the VisualizationGenerator (which includes the ReviewerAgent)
    viz_gen = VisualizationGenerator()
    
    # Example with CSV file
    csv_path = "../scrape-and-modify-data/output/sademed.csv"
    description = "Vee andmestik"
    
    try:
        print("Generating initial visualization code...")
        # Generate and process visualization code directly
        viz_gen.generate_visualization_from_csv(
            csv_path=csv_path,
            data_description=description
        )
        
        print("Visualization pipeline completed successfully!")
        
    except Exception as e:
        print(f"Error in visualization pipeline: {str(e)}")

if __name__ == "__main__":
    main()

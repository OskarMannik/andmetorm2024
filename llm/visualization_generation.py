from code_generator import VisualizationGenerator

def main():
    # Example usage
    viz_gen = VisualizationGenerator()
    
    # Example with CSV file
    csv_path = "scrape-and-modify-data\output\t_awvorm_001_curr.csv"
    description = "Sales data with product categories and customer counts over time"
    
    try:
        viz_code = viz_gen.generate_visualization_from_csv(
            csv_path=csv_path,
            data_description=description
        )
        print("Generated visualization code:")
        print(viz_code)
        
        # Optionally save the code to a file
        with open("generated_visualization.py", "w") as f:
            f.write(viz_code)
            
    except Exception as e:
        print(f"Error generating visualization: {str(e)}")

if __name__ == "__main__":
    main()
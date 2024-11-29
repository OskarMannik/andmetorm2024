from code_generator import (VisualizationGenerator, ReviewerAgent)


def main():
    # Initialize both agents
    viz_gen = VisualizationGenerator()
    reviewer = ReviewerAgent()
    
    # Example with CSV file
    csv_path = "scrape-and-modify-data\output\t_awvorm_001_curr.csv"
    description = "Sales data with product categories and customer counts over time"
    
    try:
        print("Generating initial visualization code...")
        viz_code = viz_gen.generate_visualization_from_csv(
            csv_path=csv_path,
            data_description=description
        )
        
        print("\nReviewing and correcting code...")
        corrected_code = reviewer.review_and_correct_code(viz_code, csv_path)
        
        print("\nSaving reviewed and corrected code...")
        print(corrected_code)
        with open("llm/generated_visualization.py", "w") as f:
            f.write(corrected_code)
            
        print("Successfully generated and saved visualization code!")
            
    except Exception as e:
        print(f"Error in visualization pipeline: {str(e)}")

if __name__ == "__main__":
    main()
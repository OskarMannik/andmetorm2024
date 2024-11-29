from openai import OpenAI
import pandas as pd
import os
from groq import Groq
from dotenv import load_dotenv

class VisualizationGenerator:
    '''
    def __init__(self):
        """Initialize the VisualizationGenerator with OpenAI client and model settings"""
        load_dotenv()
        self.client = OpenAI(
            api_key=os.getenv("RUNPOD_TOKEN"),
            base_url=os.getenv("RUNPOD_CHATBOT_URL"),
        )
        self.model_name = os.getenv("MODEL_NAME")
        '''
    def __init__(self):
        """Initialize the VisualizationGenerator with Groq client and model settings"""
        load_dotenv()
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
        )
        # Groq's LLM model (e.g., "mixtral-8x7b-32768")
        self.model_name = os.getenv("GROQ_MODEL_NAME", "mixtral-8x7b-32768")
    '''
    def _get_chatbot_response(self, messages, temperature=0):
        """Private method to get response from the chatbot"""
        input_messages = [
            {"role": message["role"], "content": message["content"]}
            for message in messages
        ]

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=input_messages,
            temperature=temperature,
            top_p=0.8,
            max_tokens=2000,
        ).choices[0].message.content
        
        return response
    '''

    def _get_chatbot_response(self, messages, temperature=0.2):
        """Private method to get response from Groq"""
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=2000,
        )
        
        return response.choices[0].message.content
    
    def get_csv_info(self, csv_path):
        """Extract column names, sample rows, and data info from CSV file"""
        try:
            # Read only first 5 rows to get column info and sample data
            df = pd.read_csv(csv_path, nrows=5)
            
            # Get column names
            columns = df.columns.tolist()
            
            # Get data types from the sample
            dtypes = df.dtypes.to_dict()
            dtype_info = [f"{col}: {dtype}" for col, dtype in dtypes.items()]
            
            # Get total number of rows by counting lines in CSV
            with open(csv_path, 'r') as f:
                total_rows = sum(1 for _ in f) - 1  # subtract header row
            
            # Get sample data as string
            sample_data = df.head(3).to_string()
            
            return columns, dtype_info, total_rows, sample_data
            
        except Exception as e:
            raise Exception(f"Error reading CSV file: {str(e)}")

    def generate_visualization_code(self, data_columns, sample_row, csv_filename, data_description=None):
        """Generate visualization code based on data analysis"""
        # Create a string representation of column types
        column_types = [f"{col}: {type(val).__name__}" for col, val in zip(data_columns, sample_row)]
        
        prompt = f"""Given these columns and their data types from a dataset: {column_types}
        Sample row of data: {dict(zip(data_columns, sample_row))}
        CSV filename: {csv_filename}
        {f'Additional context about the data: {data_description}' if data_description else ''}
        
        Generate Python code that creates a clear and professional visualization using matplotlib. Please:
        1. Import only pandas, matplotlib.pyplot, and numpy
        2. Include detailed comments explaining each step
        3. Choose the most appropriate chart type based on the data types:
           - For categorical vs numerical: Use bar charts
           - For time series: Use line charts
           - For multiple numerical columns: Use line or scatter plots
        4. Use this exact code to read the data: df = pd.read_csv('{csv_filename}')
        5. Include proper labels, title, and legend
        6. Set figure size to (12, 6) and include basic styling
        7. Handle any necessary data preprocessing
        8. End with plt.show()
        
        Provide only the Python code with comments."""

        messages = [{'role': 'user', 'content': prompt}]
        code = self._get_chatbot_response(messages, temperature=0.2)
        
        return code

    def generate_visualization_from_csv(self, csv_path, data_description=None):
        """Convenience method to generate visualization code directly from CSV file"""
        try:
            # Get CSV info
            df = pd.read_csv(csv_path, nrows=1)  # Read just one row for the sample
            columns = df.columns.tolist()
            sample_row = df.iloc[0].tolist()
            
            return self.generate_visualization_code(
                data_columns=columns,
                sample_row=sample_row,
                csv_filename=csv_path,
                data_description=data_description
            )
        except Exception as e:
            raise Exception(f"Error reading CSV file: {str(e)}")
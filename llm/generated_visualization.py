import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('../scrape-and-modify-data/output/t_awtabel002_02_curr copy.csv')

# Select a specific row of data to visualize (in this case, the first row)
row_data = df.iloc[0]

# Extract the month names and corresponding values from the row
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
month_values = [row_data['january'], row_data['february'], row_data['march'], 
                 row_data['april'], row_data['may'], row_data['june'], 
                 row_data['july'], row_data['august'], row_data['september'], 
                 row_data['october'], row_data['november'], row_data['december']]

# Create a line plot to visualize the monthly data
plt.figure(figsize=(10, 6))  # Set the figure size
plt.plot(month_names, month_values, marker='o')  # Create the line plot with markers

# Set the title and labels
plt.title('Monthly Water Data for {}'.format(row_data['water_catchment_name']))
plt.xlabel('Month')
plt.ylabel('Water Volume')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

plt.savefig('output_visualization.png')

# Display the plot
plt.show()
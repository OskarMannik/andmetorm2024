# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset from the CSV file
# The CSV file is located in the specified path and has a header row
data = pd.read_csv('../scrape-and-modify-data/output/sademed.csv')

# The user requires a yearly comparison, so we will create a line chart
# to visualize the 'sademete_hulk_mm' (amount of precipitation in mm) over the years
# We will use the 'aasta' (year) column as the x-axis and 'sademete_hulk_mm' as the y-axis

# Create the line chart
plt.figure(figsize=(10, 6))  # Set the figure size
plt.plot(data['aasta'], data['sademete_hulk_mm'], marker='o')  # Create the line chart with markers

# Add title and labels
plt.title('Yearly Comparison of Precipitation Amount')  # Set the title
plt.xlabel('Year')  # Set the x-axis label
plt.ylabel('Precipitation Amount (mm)')  # Set the y-axis label

# Add grid lines for better readability
plt.grid(True)

# Save the visualization as a PNG file
plt.savefig('output_visualization.png')

# Display the chart
plt.show()
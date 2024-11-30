# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file into a pandas DataFrame
# The CSV file is located in the specified path and has a header row
df = pd.read_csv('../scrape-and-modify-data/output/sademed.csv')

# The user requires a yearly comparison, so we'll create a line plot
# to visualize the 'sademete_hulk_mm' (precipitation amount in mm) over the years
plt.figure(figsize=(10, 6))  # Set the figure size for better readability

# Create the line plot with 'aasta' (year) on the x-axis and 'sademete_hulk_mm' on the y-axis
plt.plot(df['aasta'], df['sademete_hulk_mm'], marker='o')  # Add markers for each data point

# Set the title and labels for the axes
plt.title('Yearly Precipitation Amount in mm')  # Set the title based on the user's requirements
plt.xlabel('Year')  # Set the x-axis label
plt.ylabel('Precipitation Amount (mm)')  # Set the y-axis label

# Save the visualization as a PNG file
plt.savefig('output_visualization.png')

# Display the plot
plt.show()
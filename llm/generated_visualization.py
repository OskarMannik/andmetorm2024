# Importing the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Loading the data from the CSV file
data = pd.read_csv('./data.csv')

# Since the user requirements are to display the data distribution as a histogram,
# we will select a numerical column for the visualization.
# Here, I'm choosing 'aastakokku' (total quantity) column. You can change it if needed.
column_to_visualize = 'aastakokku'

# Preparing the data for visualization
data_to_visualize = data[column_to_visualize]

# Checking for missing values
if data_to_visualize.hasnans:
    # If there are missing values, we will fill them using the mean value of the column
    data_to_visualize = data_to_visualize.fillna(data_to_visualize.mean())

# Creating the histogram
plt.hist(data_to_visualize, bins=20, edgecolor='black')

# Setting the plot title, x-axis label, and y-axis label
plt.title('Data Distribution of ' + column_to_visualize)
plt.xlabel(column_to_visualize)
plt.ylabel('Frequency')

# Adding gridlines
plt.grid(axis='y', linestyle='--')

# Saving the visualization as 'output_visualization.png'
plt.savefig('output_visualization.png')

# Displaying the plot
plt.show()
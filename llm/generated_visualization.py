# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV file
data = pd.read_csv('./data/data.csv')

# Filter the data for 2022 and 2023
data_2022 = data[data['aruandeaasta'] == 2022]
data_2023 = data[data['aruandeaasta'] == 2023]

# Calculate the total for each month in 2022 and 2023
months = ['jaanuar', 'veebruar', 'marts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember']
total_2022 = data_2022[months].sum()
total_2023 = data_2023[months].sum()

# Create a line plot to compare the total for each month in 2022 and 2023
plt.figure(figsize=(10,6))
plt.plot(months, total_2022, label='2022')
plt.plot(months, total_2023, label='2023')

# Add title and labels
plt.title('Comparison of Total for Each Month in 2022 and 2023')
plt.xlabel('Month')
plt.ylabel('Total')

# Add legend
plt.legend()

# Save the visualization as 'output_visualization.png'
plt.savefig('output_visualization.png')

# Display the plot
plt.show()
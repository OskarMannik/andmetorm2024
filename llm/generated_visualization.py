# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV file
# The CSV file is assumed to be in the same directory as the script
# The 'sep' parameter is set to ',' to specify that the values are comma-separated
data = pd.read_csv('../scrape-and-modify-data/output/t_awtabel002_02_curr copy.csv')

# Filter the data to only include the years 2022 and 2023
# This is based on the user's requirement to compare these two years
data_2022 = data[data['reporting_year'] == 2022]
data_2023 = data[data['reporting_year'] == 2023]

# Calculate the total for each month in 2022 and 2023
# This is done by summing up the values for each month across all stations
total_2022 = data_2022[['january', 'february', 'march', 'april', 'may', 'june', 
                        'july', 'august', 'september', 'october', 'november', 'december']].sum()
total_2023 = data_2023[['january', 'february', 'march', 'april', 'may', 'june', 
                        'july', 'august', 'september', 'october', 'november', 'december']].sum()

# Create a line plot to compare the total for each month in 2022 and 2023
# The x-axis represents the months, and the y-axis represents the total
plt.figure(figsize=(10,6))  # Set the figure size
plt.plot(total_2022.index, total_2022.values, label='2022')  # Plot the data for 2022
plt.plot(total_2023.index, total_2023.values, label='2023')  # Plot the data for 2023
plt.xlabel('Month')  # Set the x-axis label
plt.ylabel('Total')  # Set the y-axis label
plt.title('Comparison of Total by Month in 2022 and 2023')  # Set the title
plt.legend()  # Display the legend
plt.grid(True)  # Display the grid
plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability

# Save the plot as a PNG file
plt.savefig('output_visualization.png')

# Display the plot
plt.show()
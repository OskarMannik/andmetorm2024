# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reading the csv file
data = pd.read_csv('../scrape-and-modify-data/output/t_awtabel002_02_curr.csv')

# Commenting out unnecessary columns
# data = data[['reporting_year', 'year_total']]

# Rename columns for better understanding
data = data.rename(columns={'reporting_year': 'Year', 'year_total': 'Total Annual Water Flow Volume'})

# Plotting the data
plt.figure(figsize=(10, 5)) # Set the size of the figure
plt.title('Total Annual Water Flow Volume by Year') # Add a title
plt.xlabel('Year') # Label the x-axis
plt.ylabel('Total Annual Water Flow Volume') # Label the y-axis

# Create a line plot
plt.plot(data['Year'], data['Total Annual Water Flow Volume'], marker='o') # Use circles as markers

# Format the x-axis to make it more readable
plt.gcf().autofmt_xdate() # This automatically rotates and aligns the x-axis labels

# Save the plot
plt.savefig('output_visualization.png')


plt.show()
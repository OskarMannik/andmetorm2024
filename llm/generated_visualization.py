# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reading the csv file
data = pd.read_csv('../scrape-and-modify-data/output/t_awtabel002_02_curr.csv')

# Cleaning the data by removing NaN values
data = data.dropna()

# Calculating the average annual water flow
average_year_total = np.mean(data['year_total'])

# Creating a new dataframe with the year and year_total columns
average_data = pd.DataFrame({
    'reporting_year': [2022] + [2022 + i for i in range(1, 6)],  # Adding 5 years starting from 2022
    'year_total': [average_year_total] * 6  # Repeating the average year_total 6 times
})

# Concatenating the original dataframe with the new dataframe
data = pd.concat([data, average_data], ignore_index=True)

# Plotting the data using a line plot
plt.figure(figsize=(10, 6))
plt.plot('reporting_year', 'year_total', data=data)
plt.scatter('reporting_year', 'year_total', data=average_data)

# Setting the title and labels
plt.title('Average Annual Water Flow (Vee andmestik)')
plt.xlabel('Reporting Year')
plt.ylabel('Year Total (m3)')

# Adding a legend
plt.legend(['Actual Data', 'Average'])

# Saving the plot as a png file
plt.savefig('output_visualization.png')

# Displaying the plot
plt.show()
# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reading the csv file
data = pd.read_csv('../scrape-and-modify-data/output/t_awtabel002_02_curr.csv')

# Filtering the data for the reporting year 2023
filtered_data = data[data['aruandeaasta'] == 2023]

# Selecting the first row of the filtered data
row = filtered_data.iloc[0]

# Extracting the data for the selected row
extracted_data = row.drop(
    ['aruandeaasta', 'annual_report_id', 'veehaardekood', 'veehaardenimetus'])

print(extracted_data)

# Converting the extracted data to a numpy array for plotting
data_array = extracted_data.to_numpy()

# Creating a figure and setting the size
plt.figure(figsize=(12, 6))

# Creating a bar chart with months on the x-axis and the corresponding values on the y-axis
plt.bar(range(len(data_array)), data_array)

# Setting the x-axis label
plt.xlabel('Months')

# Setting the y-axis label
plt.ylabel('Values')

# Setting the title of the chart
plt.title('Vee andmestik for the reporting year 2023')

# Adding ticks on the x-axis with month names
# plt.xticks(range(len(data_array)), ['Januar', 'Veebruar', 'Marts', 'Aprill', 'Mai',
#            'Juuni', 'Juuli', 'August', 'September', 'Oktoober', 'November', 'Detsember'])

# Saving the visualization as 'output_visualization.png'
plt.savefig('output_visualization.png')

# Displaying the plot
plt.show()

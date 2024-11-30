# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Loading the dataset from the CSV file
data = pd.read_csv('./llm/data.csv')

# Since the user didn't specify which column to use for the histogram,
# I'll choose a column with numerical data and no missing values.
# I'll use the 'aastakokku' column which represents the total quantity for the year.

# Preparing the data for the histogram
aastakokku_data = data['aastakokku']
aastakokku_data = aastakokku_data.dropna()  # Dropping missing values

# Creating the histogram
plt.hist(aastakokku_data, bins=20)  # Using 20 bins for better visualization
plt.title('Data Distribution - Total Quantity for the Year')  # Adding a title
plt.xlabel('Total Quantity')  # Labeling the x-axis
plt.ylabel('Frequency')  # Labeling the y-axis

# Formatting the histogram for better readability
plt.xticks(np.arange(0, 350000, step=50000))  # Setting xticks every 50,000 units
plt.yticks(np.arange(0, 40, step=5))  # Setting yticks every 5 units

# Saving the visualization as 'output_visualization.png'
plt.savefig('output_visualization.png')

# Displaying the plot
plt.show()
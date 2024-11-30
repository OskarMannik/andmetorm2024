# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Loading the dataset from the CSV file
data = pd.read_csv('./data.csv')

# Since the data type of 'aastakokku' column is float, it might contain some null values.
# Let's replace those null values with the mean of the column so that it doesn't affect our histogram.
data['aastakokku'].fillna(data['aastakokku'].mean(), inplace=True)

# Now, let's create a histogram for the 'aastakokku' column which represents the total stock of fish in a year.
plt.hist(data['aastakokku'], bins=50, edgecolor='black')

# Adding title, labels, and grid
plt.title('Distribution of Total Stock of Fish in a Year')
plt.xlabel('Total Stock of Fish')
plt.ylabel('Frequency')
plt.grid(True)

# Formatting the x-axis ticks
plt.xticks(np.arange(0, 350000, step=50000))

# Saving the visualization as 'output_visualization.png'
plt.savefig('output_visualization.png')

# Displaying the plot
plt.show()
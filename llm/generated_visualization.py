# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reading the data from the csv file
df = pd.read_csv('data/Sales_Data_with_Categorical_Columns.csv')

# Let's check the first few rows of the dataset
print(df.head())

# Since we have both categorical and numerical data, a good choice would be to use a bar chart
# First, let's see how sales are distributed across different product categories
# Preprocessing: Group the data by Product_Category and calculate the sum of Sales
sales_by_category = df.groupby('Product_Category')['Sales'].sum().reset_index()

# Creating a bar chart
plt.figure(figsize=(12, 6))
plt.bar(sales_by_category['Product_Category'], sales_by_category['Sales'])
plt.title('Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45) # Rotate x-axis labels for better readability
plt.show()

# Now, let's see how sales are distributed across different regions over time
# Preprocessing: Pivot the data to create a multi-index dataframe with Region and Date as the index
sales_by_region_date = df.pivot_table(index=['Region', 'Date'], values='Sales')

# Creating a line chart
plt.figure(figsize=(12, 6))
plt.plot(sales_by_region_date.index.get_level_values(1), sales_by_region_date.values, marker='o')
plt.title('Sales by Region Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0)) # Legend in the top-right corner
plt.show()

# Lastly, let's see the relationship between Revenue and Customer_Count
# Creating a scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(df['Customer_Count'], df['Revenue'])
plt.title('Revenue vs Customer Count')
plt.xlabel('Customer Count')
plt.ylabel('Revenue')
plt.show()
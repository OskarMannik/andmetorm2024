# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data
df = pd.read_csv('Sales_Data_with_Categorical_Columns.csv')

# Let's check if there are any missing values in the numerical columns
numerical_columns = ['Sales', 'Revenue', 'Customer_Count']
if df[numerical_columns].isnull().values.any():
    print("Missing values found in numerical columns. Replacing them with the mean.")
    df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].mean())

# Since we have a time series data, let's create a line plot for Sales over time
plt.figure(figsize=(12, 6))

# Set the style
plt.style.use('ggplot')

# Plot Sales over time
plt.plot('Date', 'Sales', data=df, marker='o', color='blue', linewidth=1, markersize=4, label='Sales')

# Set the title and labels
plt.title("Sales Data Over Time", fontsize=18, fontweight=0, color='black')
plt.xlabel("Date", fontsize=14, fontweight=0, color='black')
plt.ylabel("Sales", fontsize=14, fontweight=0, color='black')

# Add grid
plt.grid(True, linestyle='--', linewidth=0.5, color='lightgray')

# Add legend
plt.legend(loc='upper left', fontsize=12)

# Show the plot
plt.show()

# Now, let's create a bar chart for Sales by Product_Category
plt.figure(figsize=(12, 6))

# Set the style
plt.style.use('ggplot')

# Group Sales by Product_Category and calculate the sum
sales_by_category = df.groupby('Product_Category')['Sales'].sum().reset_index()

# Plot Sales by Product_Category
plt.bar('Product_Category', 'Sales', data=sales_by_category, color='blue', edgecolor='black', linewidth=1)

# Set the title and labels
plt.title("Sales by Product Category", fontsize=18, fontweight=0, color='black')
plt.xlabel("Product Category", fontsize=14, fontweight=0, color='black')
plt.ylabel("Sales", fontsize=14, fontweight=0, color='black')

# Add grid
plt.grid(True, linestyle='--', linewidth=0.5, color='lightgray')

# Add value labels on the bars
for i, v in enumerate(sales_by_category['Sales']):
    plt.text(i, v+5, str(v), ha='center')

# Add legend
plt.legend(loc='upper left', fontsize=12)

# Show the plot
plt.show()
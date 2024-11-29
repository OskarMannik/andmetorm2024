# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data from the CSV file with appropriate parameters and error handling
df = pd.read_csv('Sales_Data_with_Categorical_Columns.csv', on_bad_lines='skip')

# Check the first few rows of the dataset
print(df.head())

# Convert string numbers to appropriate numeric types
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')
df['Customer_Count'] = pd.to_numeric(df['Customer_Count'], errors='coerce')

# Handle categorical data correctly
df['Date'] = pd.to_datetime(df['Date'])
df['Region'] = df['Region'].astype('category')
df['Product_Category'] = df['Product_Category'].astype('category')

# Deal with potential missing or invalid values
df = df.dropna()

# Time series plot for Sales column
plt.figure(figsize=(12, 6))
plt.style.use('ggplot')
plt.plot('Date', 'Sales', data=df)
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# Bar chart for Revenue by Region
plt.figure(figsize=(12, 6))
plt.style.use('ggplot')
revenue_by_region = df.groupby('Region')['Revenue'].mean()
plt.bar(revenue_by_region.index, revenue_by_region.values)
plt.title('Average Revenue by Region')
plt.xlabel('Region')
plt.ylabel('Revenue')
plt.show()

# Bar chart for Customer_Count by Product_Category
plt.figure(figsize=(12, 6))
plt.style.use('ggplot')
customer_count_by_category = df.groupby('Product_Category')['Customer_Count'].mean()
plt.bar(customer_count_by_category.index, customer_count_by_category.values)
plt.title('Average Customer Count by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Customer Count')
plt.show()
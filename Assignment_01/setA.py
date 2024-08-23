import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data for the DataFrame
data = {
    'name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'age': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'percentage': [85.5, 92.3, 78.6, 88.4, 79.5, 91.2, 85.7, 90.1, 87.6, 83.4]
}
# Create the DataFrame
df = pd.DataFrame(data)
# View the DataFrame
print(df)

#A2
# Print the shape of the DataFrame
print("Shape of the DataFrame:", df.shape)
# Print the number of rows and columns
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
# Print the data types of each column
print("\nData types of each column:")
print(df.dtypes)
# Print the feature names (column names)
print("\nFeature names (column names):")
print(df.columns.tolist())
# Print the description of the DataFrame
print("\nDescription of the DataFrame:")
print(df.describe(include='all'))

#A3
# Print basic statistical details of the data
print("\nBasic statistical details of the data:")
print(df.describe())

#A4
# Add 5 rows with duplicate and missing values
add_data = {
    'name': ['K', 'L', None, 'N', 'O'],
    'age': [23, 30, 25, None, 29],
    'percentage': [85.5, None, 78.6, 79.5, 91.2]
}
add_df = pd.DataFrame(add_data)
# add data to the original DataFrame
df = pd.concat([df, add_df], ignore_index=True)
# Add a new column 'remarks' with empty values
df['remarks'] = ""
# Display the updated DataFrame
print(df)

#A5
# Number of observations
num_obser = df.shape[0]
# Number of missing values
num_missing_values = df.isnull().sum().sum()
# Number of duplicate rows
num_duplicate_rows = df.duplicated().sum()
# Display the results
print(f"Number of observations: {num_obser}")
print(f"Number of missing values: {num_missing_values}")
print(f"Number of duplicate rows: {num_duplicate_rows}")

#A6
# add data to the original DataFrame
df = pd.concat([df, add_df], ignore_index=True)
# Add a new column 'remarks' with empty values
df['remarks'] = ""
# Display the updated DataFrame
print(df)
# Drop the 'remarks' column
df = df.drop(columns=['remarks'])
# Drop all rows with null or empty values
df = df.dropna()
# Print the modified DataFrame
print( )
print(df)

#A7
# Generate a line plot of name vs percentage
plt.figure(figsize=(10, 6))
plt.plot(df['name'], df['percentage'], marker='o', linestyle='-')
plt.xlabel('Name')
plt.ylabel('Percentage')
plt.title('Name vs Percentage')
plt.grid(True)
plt.tight_layout() #Adjust the layout fot better fit
plt.show()

#A8
# Generate a scatter plot of name vs percentage
plt.figure(figsize=(10, 6))
plt.scatter(df['name'], df['percentage'], c='blue', marker='o')
plt.xlabel('Name')
plt.ylabel('Percentage')
plt.title('Name vs Percentage')
plt.grid(True)
plt.tight_layout()  # Adjust layout for better fit
plt.show()
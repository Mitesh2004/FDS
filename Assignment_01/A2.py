import pandas as pd

data = {
    'name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'age': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'percentage': [85.5, 92.3, 78.6, 88.4, 79.5, 91.2, 85.7, 90.1, 87.6, 83.4]
}

# Create the DataFrame
df = pd.DataFrame(data)

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
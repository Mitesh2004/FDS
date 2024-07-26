import pandas as pd

data = {
    'name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'age': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'percentage': [85.5, 92.3, 78.6, 88.4, 79.5, 91.2, 85.7, 90.1, 87.6, 83.4]
}

# Create the initial DataFrame
df = pd.DataFrame(data)

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
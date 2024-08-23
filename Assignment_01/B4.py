import pandas as pd
import numpy as np

# Replace 'path_to_your_file' with the actual path to your CSV file
df = pd.read_csv(r'h:\archive\SOCR-HeightWeight.csv')

# Get the number of observations (rows)
num_observations = df.shape[0]
print(f"Number of observations: {num_observations}")

# Get the number of missing values for each column
missing_values = df.isnull().sum()
print("\nNumber of missing values in each column:\n", missing_values)

# Get the total number of NaN values in the entire DataFrame
total_nan_values = df.isnull().sum().sum()
print(f"\nTotal number of NaN values in the DataFrame: {total_nan_values}")
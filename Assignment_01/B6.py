import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
df = pd.read_csv(r'h:\archive\SOCR-HeightWeight.csv')

# Convert height from inches to meters
df['Height(Meters)'] = df['Height(Inches)'] 
# Calculate BMI and add it as a new column
# BMI formula: weight (kg) / height (m)^2
df['BMI'] = df['Weight(Pounds)'] / (df['Height(Meters)'] ** 2)

# Print the DataFrame with the new BMI column
print("\nDataFrame with BMI column:")
print(df)

# Find and print the minimum and maximum BMI values
min_bmi = df['BMI'].min()
max_bmi = df['BMI'].max()
print(f"\nMinimum value from BMI column: {min_bmi}")
print(f"Maximum value from BMI column: {max_bmi}")
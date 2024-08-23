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
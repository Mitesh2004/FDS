import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
df = pd.read_csv(r'h:\archive\SOCR-HeightWeight.csv')

#B1
# Print the first 10 rows
print("First 10 rows:")
print(df.head(10))
# Print the last 10 rows
print("\nLast 10 rows:")
print(df.tail(10))
# Print 20 random rows
print("\nRandom 20 rows:")
print(df.sample(20))

#B2
# Print DataFrame shape
print("\nShape of the DataFrame:")
print(df.shape)
# Print DataFrame size
print("\nSize of the DataFrame:")
print(df.size)
# Print DataFrame dtypes
print("\nData types of each column:")
print(df.dtypes)

#B3
# Print basic statistical details
print("\nBasic Statistical Details:")
print(df.describe())

#B4
# Print missing values and NaN values
print("\nMissing Values and NaN values:")
print(df.isnull().sum())

#B5
# Calculate BMI and add it as a new column
# Assuming the column names are 'Weight (Pounds)' and 'Height (Inches)'
df['BMI'] = df['Weight(Pounds)'] / (df['Height(Inches)'] ** 2)
# Print the DataFrame with the new BMI column
print("\nDataFrame with BMI column:")
print(df)

#B6
# Find and print the minimum and maximum BMI values
min_bmi = df['BMI'].min()
max_bmi = df['BMI'].max()
print(f"\nMinimum value from BMI column: {min_bmi}")
print(f"Maximum value from BMI column: {max_bmi}")

#B7
# Plot weight vs height
plt.figure(figsize=(8, 5))
plt.plot(df['Weight(Pounds)'], df['Height(Inches)'])
plt.scatter(df['Weight(Pounds)'], df['Height(Inches)'])
plt.title('Weight vs Height')
plt.xlabel('Weight(Pounds)')
plt.ylabel('Height(Inches)')
plt.grid(True)
plt.show()
import pandas as pd
import numpy as np

# Replace 'path_to_your_file' with the actual path to the downloaded ESV file
df = pd.read_csv(r'h:\archive\SOCR-HeightWeight.csv')

# Print the first 10 rows
print("First 10 rows:")
print(df.head(10))

# Print the last 10 rows
print("\nLast 10 rows:")
print(df.tail(10))

# Print 20 random rows
print("\nRandom 20 rows:")
print(df.sample(20))
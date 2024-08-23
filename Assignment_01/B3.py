import pandas as pd
import numpy as np

# Replace 'path_to_your_file' with the actual path to your CSV file
df = pd.read_csv(r'h:\archive\SOCR-HeightWeight.csv')

# Display basic statistical details
print("Basic Statistical Details:\n")
print(df.describe())
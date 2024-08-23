import pandas as pd
import numpy as np

# Replace 'path_to_your_file' with the actual path to your CSV file
df = pd.read_csv(r'h:\archive\SOCR-HeightWeight.csv')

# Display the shape of the DataFrame (rows, columns)
print("Shape of the DataFrame:", df.shape)

# Display the size of the DataFrame (total number of elements)
print("Size of the DataFrame:", df.size)

# Display the datatypes of each column
print("Data types of each column:\n", df.dtypes)
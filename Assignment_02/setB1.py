import pandas as pd

# Load the iris dataset from the URL
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv(url, header=None, names=column_names)

# Display the first few rows of the dataset
print("Iris Dataset:")
print(df.head())

# Take a sample from the dataset
ex_df = df.sample(frac=0.1)  # Sample 10% of the data
print("\nSample of the Dataset:")
print(ex_df)

# Display maximum and minimum values of all numeric attributes
max = df.max(numeric_only=True)
min = df.min(numeric_only=True)

print("\nMaximum values of all numeric attributes:")
print(max)
print("\nMinimum values of all numeric attributes:")
print(min)

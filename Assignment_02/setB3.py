import pandas as pd

# Read the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv(url, header=None, names=column_names)

# Calculate and display column-wise mean
print("Column-wise Mean:")
print(df.mean(numeric_only=True))
print("\n")

# Calculate and display column-wise median
print("Column-wise Median:")
print(df.median(numeric_only=True))

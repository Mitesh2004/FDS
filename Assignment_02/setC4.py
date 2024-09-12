import pandas as pd

# URL of the dataset (Iris dataset)
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Define column names
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Read the CSV file into a DataFrame
df = pd.read_csv(url, header=None, names=columns)

# Describe the dataset
print("Dataset Description:")
print(df.describe(include='all'))

# Compute the mean value of numeric attributes
print("\nMean values of numeric attributes:")
print(df.mean(numeric_only=True))

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())
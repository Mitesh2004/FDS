import pandas as pd

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/nursery/nursery.data'

columns = ['parents', 'has_nurs', 'form', 'children', 'housing', 'finance', 'social', 'health', 'class']

df = pd.read_csv(url, header=None, names=columns)

print("First few rows of the dataset:")
print(df.head())

split_attribute = 'parents'

grouped = df.groupby(split_attribute)

means = grouped.mean(numeric_only=True)
print(f"\nComparing means based on the '{split_attribute}' attribute:")
print(means)
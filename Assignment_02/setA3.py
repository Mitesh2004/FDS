import pandas as pd

data = {'A': [10, 20, 30, 40, 50],
        'B': [15, 25, 35, 45, 55],
        'C': [5, 10, 15, 20, 25] }

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

mean = df.mean()
print("\nMean values:")
print(mean)

range = df.max() - df.min()
print("\nRange values:")
print(range)

IQR = df.quantile(0.75) - df.quantile(0.25)
print("\nIQR values:")
print(IQR)


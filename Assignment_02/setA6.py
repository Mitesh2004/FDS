import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Graduation Percentage': [85, 90, 78, 92, 88],
    'Age': [22, 23, 21, 24, 22]
}
df = pd.DataFrame(data)

avgage = df['Age'].mean()
per = df['Graduation Percentage'].mean()

# Display results
print("Average age:",avgage)
print("Average graduation percentage:",per)

# Describe statistics
print(df.describe())

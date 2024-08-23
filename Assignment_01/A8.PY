import pandas as pd
import matplotlib.pyplot as plt

data = {
    'name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'age': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'percentage': [85.5, 92.3, 78.6, 88.4, 79.5, 91.2, 85.7, 90.1, 87.6, 83.4]
}

# Create the initial DataFrame
df = pd.DataFrame(data)

# Add 5 rows with duplicate and missing values
add_data = {
    'name': ['K', 'L', None, 'N', 'O'],
    'age': [23, 30, 25, None, 29],
    'percentage': [85.5, None, 78.6, 79.5, 91.2]
}

add_df = pd.DataFrame(add_data)

# add data to the original DataFrame
df = pd.concat([df, add_df], ignore_index=True)

# Add a new column 'remarks' with empty values
df['remarks'] = ""

# Display the updated DataFrame
print(df)
# Drop the 'remarks' column
df = df.drop(columns=['remarks'])

# Drop all rows with null or empty values
df = df.dropna()

# Generate a scatter plot of name vs percentage
plt.figure(figsize=(10, 6))
plt.scatter(df['name'], df['percentage'], c='blue', marker='o')
plt.xlabel('Name')
plt.ylabel('Percentage')
plt.title('Name vs Percentage')
plt.grid(True)
plt.tight_layout()  # Adjust layout for better fit
plt.show()
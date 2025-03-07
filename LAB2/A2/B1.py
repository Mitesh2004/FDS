'''
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Read the dataset
df = pd.read_csv('Market_Basket_Optimisation.csv')

# Step 2: Preprocess the data
df.dropna()

# Step 3: Convert categorical values
df_encoded = pd.get_dummies(df)

# Step 4: Apply Apriori algorithm
frequent_itemsets = apriori(df_encoded, min_support=0.1, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

# Extract support and confidence values
support_values = rules['support']
confidence_values = rules['confidence']

# Display results
print("Frequent Itemsets:")
print(frequent_itemsets) 

print("\nconfidence Rules:")
print(confidence_values)
'''

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules


df = pd.read_csv('Market_Basket_Optimisation.csv')


'''
# Display dataset info
print("Dataset Information:")
print(df.info())

# Preprocessing: Drop null values
df.dropna(inplace=True)

# Convert categorical values to one-hot encoding
items = sorted(set(item for transaction in df.values for item in str(transaction).split(',')))
df_encoded = pd.DataFrame([{item: (item in str(transaction).split(',')) for item in items} for transaction in df.values])

# Apply Apriori algorithm with different min_support values
for min_sup in [0.4, 0.6]:
    print(f'\nFrequent Itemsets for min_support = {min_sup}:')
    frequent_itemsets = apriori(df_encoded, min_support=min_sup, use_colnames=True)
    print(frequent_itemsets)
    
    print('\nAssociation Rules:')
    rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)
    print(rules)
'''

# Convert dataset into a one-hot encoded format
df.fillna(0, inplace=True)  # Replace NaN with 0
df = df.applymap(lambda x: 1 if isinstance(x, str) else 0)  # Convert items to binary format

# Apply Apriori algorithm with different min_support values
for min_sup in [0.5]:  # Use lower min_support values since dataset is large
    print(f'\nFrequent Itemsets for min_support = {min_sup}:')
    frequent_itemsets = apriori(df, min_support=min_sup, use_colnames=True)
    print(frequent_itemsets)

    if not frequent_itemsets.empty:
        print('\nAssociation Rules:')
        rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)
        print(rules)
    else:
        print("No frequent itemsets found for this min_support.")

        

'''
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
# Sample transactions data
transactions = [
    ['milk', 'bread', 'eggs'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter'],
    ['milk', 'eggs'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter'],
    ['milk', 'bread', 'butter', 'eggs'],
    ['milk', 'bread'],
    ['bread', 'butter', 'eggs']
]
#print(transactions)
# Convert transactions to one-hot encoded format
encoder = TransactionEncoder()
onehot = encoder.fit_transform(transactions)
df = pd.DataFrame(onehot, columns=encoder.columns_)

# Find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)
print(frequent_itemsets)
# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)
#print(rules)
# Extract support and confidence values
support_values = rules['support']
confidence_values = rules['confidence']

print("Support Values:")
print(support_values)

print("\nConfidence Values:")
print(confidence_values)
'''

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Creating dataset
dataset = [
    ['Laptop', 'Mouse', 'Keyboard'],
    ['Phone', 'Charger', 'Earphones'],
    ['Laptop', 'Mouse', 'USB Drive'],
    ['Phone', 'Charger', 'Case'],
    ['Laptop', 'Charger', 'USB Drive', 'Mouse'],
    ['Laptop', 'Mouse', 'Keyboard', 'USB Drive'],
    ['Phone', 'Charger', 'Earphones', 'Power Bank'],
    ['Laptop', 'Mouse'],
    ['Phone', 'Case', 'Earphones'],
    ['Laptop', 'USB Drive', 'Charger']
]
# Converting dataset into a DataFrame
items = sorted(set(item for transaction in dataset for item in transaction))
df = pd.DataFrame([{item: (item in transaction) for item in items} for transaction in dataset])

# Applying Apriori algorithm with different min_support values
for min_sup in [0.1, 0.2, 0.3, 0.4]:
    print(f'\nFrequent Itemsets for min_support = {min_sup}:')
    frequent_itemsets = apriori(df, min_support=min_sup, use_colnames=True)
    print(frequent_itemsets)

    print('\nAssociation Rules:')
    rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)
    print(rules)



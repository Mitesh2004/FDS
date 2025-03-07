'''
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

# Create the dataset
data = [
    ['Bread', 'Milk'],
    ['Bread', 'Diaper', 'Beer', 'Eggs'],
    ['Milk', 'Diaper', 'Beer', 'Cake'],
    ['Bread', 'Milk', 'Diaper', 'Beer'],
    ['Bread', 'Milk', 'Diaper', 'Coke']
]

# Convert categorical values into numeric format
te = TransactionEncoder()
te_ary = te.fit_transform(data)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Apply Apriori algorithm with min_sup=2 (at least 2 transactions)
frequent_itemsets = apriori(df, min_support=2/len(df), use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

support_values = rules['support']
confidence_values = rules['confidence']


# Print frequent itemsets and association rules
print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nconfidence Rules:")
print(support_values)
'''

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Creating dataset
dataset = [
    ['Bread', 'Milk'],
    ['Bread', 'Diaper', 'Beer', 'Eggs'],
    ['Milk', 'Diaper', 'Beer', 'Coke'],
    ['Bread', 'Milk', 'Diaper', 'Beer'],
    ['Bread', 'Milk', 'Diaper', 'Coke']
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


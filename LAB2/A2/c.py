import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Sample dataset (Groceries dataset)
dataset = [
    ['milk', 'bread', 'nuts', 'apple'],
    ['milk', 'bread', 'nuts'],
    ['milk', 'bread'],
    ['milk', 'bread', 'apple'],
    ['bread', 'apple'],
    ['milk', 'bread', 'apple', 'banana'],
    ['milk', 'bread', 'banana']
]

# Step 1: Convert the dataset into the required format
te = TransactionEncoder()
te_array = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_array, columns=te.columns_)

# Step 2: Apply Apriori algorithm
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)

# Step 3: Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# Display the results
print("Frequent Itemsets:\n", frequent_itemsets)
print("\nAssociation Rules:\n", rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])


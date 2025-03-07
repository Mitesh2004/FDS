import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Load dataset (modify filename if needed)
df = pd.read_csv("groceries - groceries.csv")


# Drop unnecessary columns (first column seems to be an index)
df = df.iloc[:, 1:]

# Convert dataframe to a list of transactions
transactions = df.apply(lambda x: x.dropna().tolist(), axis=1).tolist()

# Convert transactions into a one-hot encoded DataFrame
from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# Apply Apriori algorithm with different min_support values
for min_sup in [0.05, 0.1]:
    print(f'\nFrequent Itemsets for min_support = {min_sup}:')
    frequent_itemsets = apriori(df_encoded, min_support=min_sup, use_colnames=True)
    print(frequent_itemsets)

    if not frequent_itemsets.empty:
        print('\nAssociation Rules:')
        rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)
        print(rules)
    else:
        print("No frequent itemsets found for this min_support.")

'''
# Display dataset info
print("Dataset Information:")
print(df.info())

# Preprocessing: Drop null values
df.dropna(inplace=True)

# Convert dataset into a one-hot encoded format
df.fillna(0, inplace=True)
df = df.applymap(lambda x: 1 if isinstance(x, str) else 0)

# Apply Apriori algorithm with different min_support values
for min_sup in [0.05, 0.1]:
    print(f'\nFrequent Itemsets for min_support = {min_sup}:')
    frequent_itemsets = apriori(df, min_support=min_sup, use_colnames=True)
    print(frequent_itemsets)
    
    if not frequent_itemsets.empty:
        print('\nAssociation Rules:')
        rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)
        print(rules)
    else:
        print("No frequent itemsets found for this min_support.")
'''

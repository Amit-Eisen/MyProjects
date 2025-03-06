import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Applies Apriori algorithm and generates association rules
def train_apriori(df, min_support, min_lift):
    freq_itemset = apriori(df, min_support=min_support, use_colnames=True)
    rules = association_rules(freq_itemset, metric="lift", min_threshold=min_lift)

    return freq_itemset, rules

# Remove duplicates ( Avoid A->B and B->A)
def remove_duplicate_rules(rules):
    unique_rules = []
    seen_rules = set()

    for _, row in rules.iterrows():
        rule = (frozenset(row["antecedents"]), frozenset(row["consequents"]))
        reversed_rule = (frozenset(row["consequents"]), frozenset(row["antecedents"]))

        if rule not in seen_rules and reversed_rule not in seen_rules:
            seen_rules.add(rule)
            unique_rules.append(row)



    return pd.DataFrame(unique_rules)

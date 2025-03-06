import sys
import os

sys.path.append(os.path.abspath("src"))

from src.data_preprocessing import load_data, preprocess_data
from src.apriori_algorithm import train_apriori, remove_duplicate_rules #, filter_valid_rules
from src.visualization import visualize_rules



def main():
    dataset = load_data('data/Market_Basket_Optimisation.csv')
    df = preprocess_data(dataset)

    freq_itemset, rules = train_apriori(df, min_support=0.003, min_lift=3)

    rules = remove_duplicate_rules(rules)

    # Pairs
    pair_rules = rules[(rules["antecedents"].apply(len) == 1) & (rules["consequents"].apply(len) == 1)]
    top_5_pairs = pair_rules.nlargest(10, 'lift')
    print("\n🔹 Top 5 Strongest Pairs:")
    print(top_5_pairs[['antecedents', 'consequents', 'lift', 'support', 'confidence']])
    visualize_rules(top_5_pairs, "Top 5 Strongest Pairs")

    # Triplets
    triplet_rules = rules[(rules["antecedents"].apply(len) + rules["consequents"].apply(len) == 3)]
    top_5_triplets = triplet_rules.nlargest(10, 'lift')
    print("\n🔹 Top 5 Strongest Triplets:")
    print(top_5_triplets[['antecedents', 'consequents', 'lift', 'support', 'confidence']])
    visualize_rules(top_5_triplets, "Top 5 Strongest Triplets")


if __name__ == "__main__":
    main()
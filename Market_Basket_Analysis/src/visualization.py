import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx


def visualize_rules(rules, title="Association Rules Network"):

    # Scatter plot of Support vs Confidence
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=rules["support"], y=rules["confidence"],
                    size=rules["lift"], hue=rules["lift"],
                    palette="viridis", alpha=0.7)
    plt.title("Filtered Support vs Confidence (Lift > 3, Confidence > 0.3)")
    plt.xlabel("Support")
    plt.ylabel("Confidence")
    plt.legend()
    plt.show()

    # Create Network Graph of Rules
    G = nx.DiGraph()
    for _, row in rules.iterrows():
        G.add_edge(str(row['antecedents']), str(row['consequents']), weight=row['lift'])

    plt.figure(figsize=(12, 8))
    pos = nx.circular_layout(G)  # Force-directed layout to space nodes
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=8)
    plt.title("Filtered Association Rules Network (Lift > 3, Confidence > 0.3)")
    plt.show()
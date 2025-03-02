import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Dynamically get the correct path
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../data/raw/creditcard.csv")


def explore_data():
    """Loads and explores the dataset, displaying statistics and visualizations."""

    print("🔍 Loading data...")
    df = pd.read_csv(file_path)

    # Basic information about the data
    print("\n📊 Dataset Info:")
    print(df.info())

    print("\n📈 Dataset Statistics:")
    print(df.describe())

    # Check class distribution
    print("\n🔹 Class Distribution:")
    print(df["Class"].value_counts())
    print(f"Percentage of fraud cases: {df['Class'].mean() * 100:.5f}%")

    # Plot class distribution
    plt.figure(figsize=(6, 4))
    sns.countplot(x=df["Class"], hue=df["Class"], palette=["blue", "red"], legend=False)
    plt.xticks(ticks=[0, 1], labels=["Regular", "Fraud"])
    plt.title("Class Distribution (Regular vs. Fraud)")
    plt.xlabel("Class")
    plt.ylabel("Count")
    plt.show()

    # Transaction Amount Distribution (log scale)
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Amount"], bins=50)
    plt.xscale("log")
    plt.title("Distribution of Transaction Amounts (Log Scale)")
    plt.xlabel("Amount ($)")
    plt.ylabel("Frequency")
    plt.show()

    # Correlation heatmap (show only strong correlations)
    plt.figure(figsize=(12, 8))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, cmap="coolwarm", annot=False, vmin=-1, vmax=1)
    plt.title("Feature Correlations")
    plt.show()


if __name__ == "__main__":
    explore_data()

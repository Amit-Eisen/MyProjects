import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    """Loads Titanic dataset for exploration."""
    train_df = pd.read_csv("../data/train.csv")
    test_df = pd.read_csv("../data/test.csv")
    return train_df, test_df

def eda(train_df):
    """Performs exploratory data analysis (EDA) on the Titanic dataset."""
    print("🔍 Dataset Info:")
    print(train_df.info())

    print("\n📊 Missing Values:")
    print(train_df.isnull().sum())

    print("\n🔢 Data Description:")
    print(train_df.describe())

    # Visualizations
    plt.figure(figsize=(10, 5))
    sns.countplot(x="Survived", data=train_df, hue="Survived",palette="coolwarm")
    plt.title("Survival Distribution")
    plt.show()

    plt.figure(figsize=(10, 5))
    sns.histplot(train_df["Age"].dropna(), bins=30, kde=True, color="blue")
    plt.title("Age Distribution")
    plt.show()

if __name__ == "__main__":
    train_df, test_df = load_data()
    eda(train_df)

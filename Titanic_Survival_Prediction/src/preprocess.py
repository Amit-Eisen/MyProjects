import pandas as pd
from sklearn.model_selection import train_test_split


def load_data():
    """Loads the Titanic dataset."""
    train_df = pd.read_csv("../data/train.csv")
    test_df = pd.read_csv("../data/test.csv")
    return train_df, test_df


def preprocess_data(df):
    """Preprocesses the dataset by performing feature engineering and encoding."""
    # Extract Title from Name before dropping it
    df["Title"] = df["Name"].str.extract(r"([A-Za-z]+)\.", expand=False)
    # Replace rare titles with 'Rare' and standardize common titles
    df["Title"] = df["Title"].replace(
        ['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'],
        'Rare'
    )
    df["Title"] = df["Title"].replace({"Mlle": "Miss", "Ms": "Miss", "Mme": "Mrs"})

    # Create FamilySize feature
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

    # Drop columns that are not useful after feature extraction
    df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])

    # Fill missing values in Age with the median
    df["Age"] = df["Age"].fillna(df["Age"].median())

    # Fill missing values in Embarked with the mode
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Convert categorical variables into dummy/indicator variables
    # Note: Including 'Sex', 'Embarked', and 'Title'
    df = pd.get_dummies(df, columns=["Sex", "Embarked", "Title"], drop_first=True)

    return df


def get_train_test_split():
    """
    Loads and preprocesses the training data,
    then splits it into training and test sets.
    """
    train_df, _ = load_data()
    train_df = preprocess_data(train_df)

    # Separate features and target
    X = train_df.drop(columns=["Survived"])
    y = train_df["Survived"]

    return train_test_split(X, y, test_size=0.2, random_state=42)


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = get_train_test_split()
    print("✅ Data preprocessing completed successfully.")

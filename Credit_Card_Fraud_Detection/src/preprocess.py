import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os


def preprocess_data(file_path="data/raw/creditcard.csv", save_path="data/processed/"):
    """Loads and preprocesses the dataset and saves Train/Test sets."""

    # Check if preprocessed data already exists
    if os.path.exists(f"{save_path}/X_train.npy") and os.path.exists(f"{save_path}/y_train.npy"):
        print("✅ Processed data found, skipping preprocessing...")
        return

    print("🛠 Processing data...")

    # Load dataset
    df = pd.read_csv(file_path)

    # Normalize 'Amount'
    scaler = StandardScaler()
    df["Amount"] = scaler.fit_transform(df[["Amount"]])

    # Drop 'Time'
    df.drop(columns=["Time"], inplace=True)

    # Features and target
    X = df.drop(columns=["Class"])
    y = df["Class"]

    # Train/Test split WITHOUT SMOTE
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # Save processed data
    os.makedirs(save_path, exist_ok=True)
    np.save(f"{save_path}/X_train.npy", X_train)
    np.save(f"{save_path}/X_test.npy", X_test)
    np.save(f"{save_path}/y_train.npy", y_train)
    np.save(f"{save_path}/y_test.npy", y_test)
    joblib.dump(scaler, f"{save_path}/scaler.pkl")

    print(f"✅ Train size: {X_train.shape}, Test size: {X_test.shape}")
    print("✅ Preprocessing complete. Data saved in /data/processed/")


if __name__ == "__main__":
    preprocess_data()

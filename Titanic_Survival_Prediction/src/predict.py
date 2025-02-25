import os
import pandas as pd
import joblib
from preprocess import load_data, preprocess_data


def make_predictions():
    """
    Loads and preprocesses the test dataset, uses the trained model to make predictions,
    and saves the results with PassengerId to a submission CSV.
    """
    # Load the test dataset (load_data returns train and test)
    _, test_df = load_data()

    # Extract PassengerId from the original test data before preprocessing
    passenger_ids = test_df["PassengerId"]

    # Preprocess the test dataset (PassengerId and other unnecessary columns are dropped)
    test_df = preprocess_data(test_df)

    # Load the trained model
    model = joblib.load("../models/trained_model.pkl")

    # Generate predictions using the processed test data
    predictions = model.predict(test_df)

    # Create submission DataFrame with the original PassengerId values
    submission = pd.DataFrame({
        "PassengerId": passenger_ids,
        "Survived": predictions
    })

    # Ensure that the results directory exists
    os.makedirs("../results", exist_ok=True)

    # Save the submission file
    submission.to_csv("../results/submission.csv", index=False)
    print("✅ Predictions saved to results/submission.csv.")


if __name__ == "__main__":
    make_predictions()

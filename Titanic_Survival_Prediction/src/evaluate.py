import joblib
from sklearn.metrics import accuracy_score
from preprocess import get_train_test_split


def evaluate_model():
    """
    Loads the trained model and evaluates it on the test set
    obtained from the in-memory train-test split.
    """
    # Get train/test split from the preprocessing function
    X_train, X_test, y_train, y_test = get_train_test_split()

    # Load the trained model
    model = joblib.load("../models/trained_model.pkl")

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate and print accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"🎯 Model Accuracy on test set: {accuracy:.4f}")


if __name__ == "__main__":
    evaluate_model()

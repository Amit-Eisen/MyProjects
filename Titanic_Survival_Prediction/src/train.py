import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from preprocess import get_train_test_split

def train_and_compare_models():
    """Trains and compares multiple models on the Titanic dataset."""
    # Get the training and test splits from the preprocessing function
    X_train, X_test, y_train, y_test = get_train_test_split()

    # Define models to compare
    models = {
        "Random Forest": RandomForestClassifier(n_estimators=130, random_state=42),
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=11)
    }

    results = {}

    # Train each model and evaluate accuracy on the test set
    for name, model in models.items():
        model.fit(X_train, y_train)
        accuracy = model.score(X_test, y_test)
        results[name] = accuracy
        print(f"Model: {name}, Accuracy: {accuracy * 100:.2f}%")

    # Choose the best model (highest accuracy)
    best_model_name = max(results, key=results.get)
    best_model = models[best_model_name]
    print(f"\nBest Model: {best_model_name} with accuracy {results[best_model_name] * 100:.2f}%")

    # Save the best model
    joblib.dump(best_model, "../models/trained_model.pkl")
    print("✅ Best model saved successfully.")

if __name__ == "__main__":
    train_and_compare_models()

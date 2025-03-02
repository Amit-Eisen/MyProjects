import numpy as np
import joblib
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


def evaluate_model(data_path="data/processed/", model_path="models/xgboost.pkl"):
    """Loads a trained model and evaluates its performance."""

    print("🔍 Loading model...")
    model = joblib.load(model_path)

    X_test = np.load(f"{data_path}X_test.npy")
    y_test = np.load(f"{data_path}y_test.npy")

    print("🔍 Making predictions...")
    y_pred = model.predict(X_test)

    print("\n📊 Classification Report:")
    print(classification_report(y_test, y_pred))
    print("\n📈 ROC-AUC Score:", roc_auc_score(y_test, y_pred))

    # Generate Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Regular", "Fraud"],
                yticklabels=["Regular", "Fraud"])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()


if __name__ == "__main__":
    evaluate_model()

import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import RandomizedSearchCV
import joblib
import os


def tune_xgboost(X_train, y_train):
    """Tunes XGBoost hyperparameters using RandomizedSearchCV."""
    param_grid = {
        "n_estimators": [100, 200, 300],
        "max_depth": [3, 6, 9],
        "learning_rate": [0.01, 0.05, 0.1],
        "scale_pos_weight": [100, 300, 500]
    }

    xgb = XGBClassifier(random_state=42, eval_metric="logloss")

    search = RandomizedSearchCV(
        xgb, param_distributions=param_grid,
        n_iter=10, scoring="roc_auc", cv=3, verbose=2, n_jobs=-1
    )

    search.fit(X_train, y_train)
    print("✅ Best Parameters:", search.best_params_)
    return search.best_estimator_


def train_model(data_path="data/processed/", model_path="models/xgboost.pkl", fine_tune=False):
    """Trains an XGBoost model with or without hyperparameter tuning."""

    print(f"⚙️ fine_tune={fine_tune} → Using {'Fine-Tuning' if fine_tune else 'Manual Parameters'}")

    if os.path.exists(model_path):
        print("⚠️ Removing old model and retraining...")
        os.remove(model_path)

    print("🚀 Training XGBoost model...")
    X_train = np.load(f"{data_path}/X_train.npy")
    y_train = np.load(f"{data_path}/y_train.npy")

    if fine_tune:
        print("🔍 Running Fine-Tuning...")
        model = tune_xgboost(X_train, y_train)
    else:
        print("🔧 Using manually optimized parameters...")
        best_params = {'scale_pos_weight': 500, 'n_estimators': 300, 'max_depth': 9, 'learning_rate': 0.1}
        model = XGBClassifier(**best_params, random_state=42, eval_metric="logloss")
        model.fit(X_train, y_train)

    joblib.dump(model, model_path)
    print(f"✅ Model saved to {model_path}")


if __name__ == "__main__":
    train_model(fine_tune=False)  # Change to True to run Fine-Tuning

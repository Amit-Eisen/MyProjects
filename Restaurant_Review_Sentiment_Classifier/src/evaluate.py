from sklearn.metrics import confusion_matrix, accuracy_score

def evaluate_models(models, X_test, y_test):
    """Evaluates trained models and returns performance metrics."""
    print("\n📌 Evaluating models...")

    results = {}

    for model_name, model in models.items():
        y_pred = model.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        accuracy = accuracy_score(y_test, y_pred)

        true_positives = cm[1, 1]
        true_negatives = cm[0, 0]
        false_positives = cm[0, 1]
        false_negatives = cm[1, 0]

        positive_accuracy = (true_positives / (true_positives + false_negatives) * 100) if (true_positives + false_negatives) > 0 else 0
        negative_accuracy = (true_negatives / (true_negatives + false_positives) * 100) if (true_negatives + false_positives) > 0 else 0

        results[model_name] = {
            "confusion_matrix": cm,
            "accuracy": accuracy,
            "positive_percentage": positive_accuracy,
            "negative_percentage": negative_accuracy
        }

        print(f"\n📊 {model_name.upper()} Results:")
        print(f"✅ True Positives: {true_positives} ({positive_accuracy:.2f}%)")
        print(f"✅ True Negatives: {true_negatives} ({negative_accuracy:.2f}%)")
        print(f"❌ False Positives: {false_positives}")
        print(f"❌ False Negatives: {false_negatives}")
        print(f"📌 Overall Accuracy: {accuracy:.2f}")

    return results  # ✅ תחזיר את התוצאות כדי שהן יישמרו ב-main.py

def print_results(results):
    """Formats and prints the results of model evaluation."""
    print("\n📊 Final Model Performance:")
    for model, data in results.items():
        print(f"\n📌 {model.upper()} Results:")
        print(f"✅ Positive Reviews Identified: {data['positive_percentage']:.2f}%")
        print(f"✅ Negative Reviews Identified: {data['negative_percentage']:.2f}%")
        print(f"📌 Overall Accuracy: {data['accuracy']:.2f}")

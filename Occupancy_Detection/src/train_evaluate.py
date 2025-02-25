import numpy as np
from sklearn.metrics import accuracy_score

def train_and_evaluate(classifiers, train_data, train_labels, test_data, test_labels):
    """Trains classifiers on subsets of training data and evaluates them on test data."""
    num_samples = np.arange(100, len(train_data), 100)
    accuracies = {clf_name: [] for clf_name in classifiers}

    for clf_name, clf in classifiers.items():
        for num in num_samples:
            clf.fit(train_data[:num], train_labels[:num])
            y_pred = clf.predict(test_data)
            accuracy = accuracy_score(test_labels, y_pred)
            accuracies[clf_name].append(accuracy)
        print(f"{clf_name}: {accuracies[clf_name][-1] * 100:.2f}%")

    return num_samples, accuracies

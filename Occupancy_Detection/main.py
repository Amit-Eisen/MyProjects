from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.classifiers import get_classifiers
from src.train_evaluate import train_and_evaluate
from src.plot_results import plot_accuracies

if __name__ == "__main__":
    train_path = 'data/occupancy_train.pkl'
    test_path = 'data/occupancy_test.pkl'

    data_train, data_test = load_data(train_path, test_path)
    train_data, train_labels, test_data, test_labels = preprocess_data(data_train, data_test)
    classifiers = get_classifiers()
    num_samples, accuracies = train_and_evaluate(classifiers, train_data, train_labels, test_data, test_labels)
    plot_accuracies(num_samples, accuracies)

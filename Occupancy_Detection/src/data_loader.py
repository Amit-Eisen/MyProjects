import pickle

def load_data(train_path, test_path):
    """Loads training and testing data from pickle files."""
    data_train = pickle.load(file=open(train_path, "rb"))
    data_test = pickle.load(file=open(test_path, "rb"))
    return data_train, data_test

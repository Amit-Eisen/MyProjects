from sklearn.preprocessing import StandardScaler

def preprocess_data(data_train, data_test):
    """Extracts features and labels and normalizes the training and testing data."""
    train_data = data_train['features']
    train_labels = data_train['label']
    test_data = data_test['features']
    test_labels = data_test['label']

    scaler = StandardScaler()
    train_data_scaled = scaler.fit_transform(train_data)
    test_data_scaled = scaler.transform(test_data)

    return train_data_scaled, train_labels, test_data_scaled, test_labels

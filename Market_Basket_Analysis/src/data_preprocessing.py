import pandas as pd
from mlxtend.preprocessing import TransactionEncoder


# Load dataset
def load_data(file_path):
    dataset = pd.read_csv(file_path, header=None)
    dataset = dataset.fillna("")
    return dataset


def preprocess_data(dataset):
    transactions = dataset.map(str).values.tolist()

    transactions = [[item for item in row if item.strip() != ""] for row in transactions]

    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df =pd.DataFrame(te_ary, columns=te.columns_)
    return df





import pandas as pd

def load_data(file_path="../data/instruments.csv"):
    """
    Loads the knapsack problem data from a CSV file.
    Returns a list of tuples (profit, weight).
    """
    df = pd.read_csv(file_path)
    return [tuple(x) for x in df.to_numpy()]

if __name__ == "__main__":
    data = load_data()
    print("Loaded data:", data)

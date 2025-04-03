import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Drop columns that aren't useful (e.g., id, full_name)
    df = df.drop(['id', 'full_name'], axis=1)

    # Drop rows with missing target
    df = df.dropna(subset=['click'])

    # Fill missing values
    df['age'] = df['age'].fillna(df['age'].median())
    df['gender'] = df['gender'].fillna('Unknown')
    df['device_type'] = df['device_type'].fillna('Unknown')
    df['ad_position'] = df['ad_position'].fillna('Unknown')
    df['browsing_history'] = df['browsing_history'].fillna('Unknown')
    df['time_of_day'] = df['time_of_day'].fillna('Unknown')

    # Label encode gender
    df['gender'] = LabelEncoder().fit_transform(df['gender'])

    # Use ad_position as the arm definition
    df['arm'] = df['ad_position'].astype('category').cat.codes

    # Save processed data
    df.to_csv(output_path, index=False)

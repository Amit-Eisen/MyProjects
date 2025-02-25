import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('wordnet')


def preprocess_data(file_path):
    dataset = pd.read_csv(file_path, delimiter='\t', quoting=3)

    lemmatizer = WordNetLemmatizer()
    all_stop_words = set(stopwords.words("english"))
    all_stop_words.remove("not")  # חשוב לשימור משמעות הסנטימנט

    corpus = []
    for review in dataset['Review']:
        review = re.sub('[^a-zA-Z]', ' ', review).lower().split()
        review = [lemmatizer.lemmatize(word) for word in review if word not in all_stop_words and len(word) > 2]
        corpus.append(" ".join(review))

    vectorizer = TfidfVectorizer(max_features=2000, ngram_range=(1, 1))
    X = vectorizer.fit_transform(corpus).toarray()
    y = dataset.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, vectorizer

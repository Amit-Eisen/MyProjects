from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

def get_classifiers():
    """Returns a dictionary of classifiers to be trained and evaluated."""
    return {
        'Logistic Regression': LogisticRegression(solver='liblinear', random_state=0),
        'Nearest Neighbors': KNeighborsClassifier(3),
        'Linear SVM': LinearSVC(C=0.025),
        'Gaussian SVM': SVC(gamma=0.2 , C=1),
        'Naive Bayes': GaussianNB()
    }

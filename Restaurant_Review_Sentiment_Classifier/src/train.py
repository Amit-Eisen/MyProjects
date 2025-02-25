from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

def train_models(X_train, y_train):
    models = {}

    # Random Forest
    rf_classifier = RandomForestClassifier(random_state=42)
    rf_param_grid = {'n_estimators': [100, 200, 300], 'max_depth': [None, 10, 20], 'max_features': ['sqrt', 'log2']}
    rf_grid_search = GridSearchCV(rf_classifier, rf_param_grid, cv=5, n_jobs=-1, scoring='accuracy')
    rf_grid_search.fit(X_train, y_train)
    models['rf'] = rf_grid_search.best_estimator_

    # Logistic Regression
    lr_classifier = LogisticRegression(max_iter=1000, random_state=42)
    lr_param_grid = {'C': [0.01, 0.1, 1, 10], 'solver': ['liblinear', 'lbfgs']}
    lr_grid_search = GridSearchCV(lr_classifier, lr_param_grid, cv=5, n_jobs=-1, scoring='accuracy')
    lr_grid_search.fit(X_train, y_train)
    models['lr'] = lr_grid_search.best_estimator_

    # Support Vector Machine (SVM)
    svm_classifier = SVC(probability=True, random_state=42)
    svm_param_grid = {'C': [0.01, 0.1, 1, 10], 'kernel': ['linear', 'rbf']}
    svm_grid_search = GridSearchCV(svm_classifier, svm_param_grid, cv=5, n_jobs=-1, scoring='accuracy')
    svm_grid_search.fit(X_train, y_train)
    models['svm'] = svm_grid_search.best_estimator_

    return models

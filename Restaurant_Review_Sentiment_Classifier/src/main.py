from preprocess import preprocess_data
from train import train_models
from evaluate import evaluate_models, print_results

if __name__ == "__main__":
    # עיבוד הנתונים
    X_train, X_test, y_train, y_test, vectorizer = preprocess_data('../data/Restaurant_Reviews.tsv')

    # אימון המודלים
    models = train_models(X_train, y_train)

    # הערכת המודלים והצגת התוצאות
    results = evaluate_models(models, X_test, y_test)
    print_results(results)

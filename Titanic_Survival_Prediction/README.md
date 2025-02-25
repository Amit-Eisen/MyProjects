# Titanic Survival Prediction

This project is a machine learning solution for predicting Titanic survivors. It includes data preprocessing with feature engineering, model training using multiple algorithms (Random Forest, Logistic Regression, K-Nearest Neighbors), and a comparison of their performance.

## Project Structure
```
titanic_survival_prediction/
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── gender_submission.csv
├── models/
│   └── trained_model.pkl
├── results/
│   └── submission.csv
├── src/
│   ├── eda.py
│   ├── preprocess.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── predict.py
├── .gitignore
├── README.md
└── requirements.txt
```
## Data

The dataset used in this project is the Titanic dataset from Kaggle. Since the raw data files are large and subject to Kaggle's terms of use, they are not included in this repository.

**To download the data:**
1. Create an account on [Kaggle](https://www.kaggle.com/).
2. Navigate to the [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic) competition page.
3. Download the `train.csv`, `test.csv`, and `gender_submission.csv` files.
4. Place the downloaded files into the `data/` directory in the project root.

Alternatively, you can use the Kaggle API:
```bash
kaggle competitions download -c titanic
```


## Getting Started

1. **Install Dependencies:**

   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt

2. **Run The Project:**
   
   python src/main.py

**This will run the following steps:**

 - Exploratory Data Analysis (EDA)
 - Data Preprocessing (with feature engineering)
 - Training and comparing models
 - Evaluating the best model
 - Generating predictions

## Future Improvements:
 - Enhance feature engineering (e.g., binning age, extracting more detailed titles).
 - Experiment with other models such as XGBoost or ensemble methods.
 - Further hyperparameter tuning to potentially improve accuracy. 
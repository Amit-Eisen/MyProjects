# 🚀 Credit Card Fraud Detection using XGBoost

## 🔍 Overview
This project is an **end-to-end pipeline** for detecting fraudulent credit card transactions using **machine learning**.  
We use **XGBoost**, a powerful gradient boosting algorithm, to achieve high accuracy while maintaining a **low false-positive rate**.

✅ **Dataset Source:** [Credit Card Fraud Detection – Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)  
✅ **Dataset Size:** ~284,807 transactions  
✅ **Class Imbalance:** Only **0.17%** of transactions are fraudulent.  

Since the dataset is highly imbalanced, we use **optimized hyperparameters** instead of data augmentation techniques like SMOTE, which previously led to overfitting.

---

## 📂 Project Structure
```
Credit_Card_Fraud_Detection/
│── data/ # Raw and processed data 
│ ├── raw/ # Original dataset (not uploaded to GitHub) 
│ ├── processed/ # Preprocessed and split data 
│── models/ # Trained models 
│ ├── xgboost.pkl # Final trained XGBoost model 
│── src/ # Source code 
│ ├── explore_data.py # Data exploration and visualization 
│ ├── preprocess.py # Data preprocessing (scaling, splitting) 
│ ├── train_model.py # Training XGBoost model (with and without tuning) 
│ ├── evaluate_model.py # Model evaluation and performance metrics 
│── main.py # Runs the full pipeline 
│── requirements.txt # Required libraries 
│── README.md # Project documentation 
│── .gitignore # Files to ignore in version control
```


---

## 📊 **Dataset Overview**
| Feature | Description |
|---------|------------|
| **Time** | Seconds elapsed since first transaction |
| **V1-V28** | PCA-transformed features (original features are not available) |
| **Amount** | Transaction amount |
| **Class** | 0 = Legitimate, 1 = Fraudulent |

💡 **The data is heavily imbalanced:**  
- **Non-fraudulent transactions (Class 0):** 284,315 (~99.83%)  
- **Fraudulent transactions (Class 1):** 492 (~0.17%)  

---
## **📊 Model Performance**
### **Manual Hyperparameter Optimization (Best Results)**
| Model Type | Precision (Fraud) | Recall (Fraud) | F1-Score | ROC-AUC |
|------------|------------------|---------------|---------|--------|
| **XGBoost (Manual Params)** | **0.88** | **0.85** | **0.86** | **0.923** |
| XGBoost (Fine-Tuned) | 0.87 | 0.84 | 0.85 | 0.918 |

✅ **We found that manually selecting hyperparameters gives slightly better results than Fine-Tuning.**  
✅ **However, the code allows both methods so you can experiment.**  

---
## ⚙️ **How to Run the Project**
#### **1️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```
#### **2️⃣ Run the full pipline (with manual parameters):**
```bash
python main.py
```
#### **3️⃣ Run Fine-Tuning (optional, takes longer):**
```bash
python main.py --fine_tune
```
#### **4️⃣ Evaluate the trained model:**
```bash
python src/evaluate_model.py
```

## Fine-Tuning vs. Manual Parameters:
  - **Manual Optimization:**
       - Pros:
         - Faster training
         - Better interpretability
       - Cons:
         - Requires domain knowledge


  - **Fine-Tuning (RandomizedSearchCV):**
       - Pros:
         - Automated process
         - Finds potentially better hyperparameters
       - Cons:
          - Longer runtime
          - Slight risk of overfitting

## 📈 Technologies Used
 - Python
 - XGBoost (for fraud detection)
 - Pandas & NumPy (for data processing)
 - Scikit-Learn (for model evaluation)
 - Matplotlib & Seaborn (for data visualization)
 - Joblib (for model saving/loading)

## 🚀 Future Improvements
 - Compare XGBoost with LightGBM to test performance.
 - Try AutoML (like Optuna) for hyperparameter optimization.
 - Develop a real-time fraud detection API using FastAPI.
 - Implement anomaly detection techniques (Isolation Forest, One-Class SVM).

# Market Basket Analysis Project

## 📌 Overview
This project implements **Market Basket Analysis** using the **Apriori algorithm** to identify frequent itemsets and association rules from transaction data. It analyzes which items are frequently purchased together, helping businesses make data-driven decisions.

## 🚀 Features
- **Data Preprocessing**: Cleans the dataset and converts transactions into a structured format.
- **Apriori Algorithm**: Identifies frequent itemsets and generates association rules.
- **Duplicate Rule Removal**: Ensures that redundant and reverse rules (A → B and B → A) are removed.
- **Top Association Rules**: Displays the strongest **pairs** and **triplets** of items based on *Lift*.
- **Visualizations**:
  - Scatter plots of **Support vs Confidence**.
  - **Network graphs** showing relationships between items.
- **Configurable Parameters**: Support, confidence, and lift thresholds can be adjusted.

## 📂 Project Structure
```
Market_Basket_Analysis/
│── data/
│   ├── Market_Basket_Optimisation.csv   # Sample dataset
│── src/
│   ├── data_processing.py               # Data loading & preprocessing
│   ├── apriori_algorithm.py             # Apriori implementation & rule filtering
│   ├── visualization.py                 # Graphs and data visualization
│── main.py                              # Runs the full pipeline
│── README.md                            # Project documentation
```
# 📊 Example Output

## 🔹 Top 5 Strongest Pairs
```
antecedents        consequents      lift  
(pasta)           (tomato sauce)   4.70  
(olive oil)       (whole wheat)    4.12 
```

## 🔹 Top 5 Strongest Triplets
```
antecedents                         consequents     lift  
(spaghetti, tomato sauce)          (ground beef)   4.84  
(olive oil, mineral water)          (shrimp)       4.50  
```

# ⚙️ How to Run

##  1️⃣ Install Dependencies
```bash 
pip install requirements.txt
```
## 2️⃣ Run the Project
```bash 
python main.py
```

## 🔜 Future Enhancements

 - Save results to CSV: Allow exporting association rules for further analysis.
 - Interactive Visualizations: Improve graph clarity and filtering.
 - Support Custom Datasets: Allow users to upload their own transaction data.
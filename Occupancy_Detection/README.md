# Occupancy Detection Project

This project implements several machine learning classifiers to detect whether a room is occupied or not based on sensor data. The dataset consists of various environmental measurements (e.g., temperature, humidity, light, CO2, etc.) along with a binary label indicating room occupancy (0 for empty, 1 for occupied).

## Project Structure

```
occupancy_detection/
 ├── data/ 
 │ ├── occupancy_test.pkl
 │ ├── occupancy_train.pkl # The dataset files 
 ├── src/ 
 │ ├── data_loader.py # Loads and preprocesses the dataset 
 │ ├── models.py # Defines the classifiers (e.g., Logistic Regression, Nearest Neighbors, Linear SVM, Gaussian SVM, Naive Bayes) 
 │ ├── train.py # Trains and evaluates the classifiers │ ├── visualize.py # Visualizes performance (e.g., accuracy vs. training samples) 
 │ └── main.py # Main script that runs the complete pipeline 
 ├── README.md 
 └── requirements.txt # Required Python packages
```


## Overview

The objective of this project is to build and compare various machine learning models for occupancy detection. The classifiers evaluated in this project include:

- Logistic Regression  
- Nearest Neighbors  
- Linear SVM  
- Gaussian SVM  
- Naive Bayes  

The performance of these models is measured using accuracy on a test set, and results are visualized with comparison plots.

## How to Run

1. **Install Dependencies**

   Run the following command to install all required packages:
   ```bash
   pip install -r requirements.txt
   ```
   
2. ***Run the Project:***

   From the project's root directory, run:

   python src/main.py


   ***This script will:***

 - Load and preprocess the dataset.
 - Train and evaluate each classifier.
 - Print the accuracy results.
 - Display plots comparing model performance.


## Expected Output

 - Logistic Regression:  XX.XX% Accuracy
 - Nearest Neighbors:  XX.XX% Accuracy
 - Linear SVM:         XX.XX% Accuracy
 - Gaussian SVM:       XX.XX% Accuracy
 - Naive Bayes:        XX.XX% Accuracy

   Additionally, a plot will be generated showing the performance of each classifier.


## Future Improvements
 - Hyperparameter Tuning: Experiment with different hyperparameters for each model to further improve performance.
 - Feature Engineering: Explore additional feature selection or extraction techniques.
 - Ensemble Methods: Consider combining multiple classifiers for potentially better accuracy.
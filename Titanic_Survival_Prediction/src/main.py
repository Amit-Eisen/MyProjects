import os

print("🚀 Starting the project...")

# Run Exploratory Data Analysis (EDA)
print("🔍 Running EDA...")
os.system("python eda.py")

# Run data preprocessing
print("🧹 Running data preprocessing...")
os.system("python preprocess.py")

# Train the model
print("🤖 Training the model...")
os.system("python train.py")

# Evaluate the model
print("📊 Evaluating the model...")
os.system("python evaluate.py")

# Make predictions and generate submission
print("🔮 Generating predictions...")
os.system("python predict.py")

print("✅ Project executed successfully!")

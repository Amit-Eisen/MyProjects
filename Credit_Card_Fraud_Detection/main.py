from src.explore_data import explore_data
from src.preprocess import preprocess_data
from src.train_model import train_model
from src.evaluate_model import evaluate_model


def main(fine_tune=False):
    """Runs the full fraud detection pipeline."""

    print("🔍 Running Exploratory Data Analysis...")
    explore_data()

    print("🛠 Preprocessing data...")
    preprocess_data()

    print("🚀 Training the model...")
    train_model(fine_tune=fine_tune)  # Change to True to run Fine-Tuning

    print("📊 Evaluating the model...")
    evaluate_model()

    print("✅ Pipeline completed successfully!")


if __name__ == "__main__":
    main(fine_tune=False)  # Change to True to run Fine-Tuning

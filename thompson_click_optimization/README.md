# Thompson Sampling with Ad Click Dataset

This project applies the Thompson Sampling algorithm to a cleaned ad click dataset. It includes a full data preprocessing pipeline and models a multi-armed bandit problem using ad position as the arm.

## How to run
1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the project:
```
python main.py
```

## Files Structure
- `data/`: Contains raw and processed datasets.
- `src/`: Contains preprocessing, ThompsonSampler, Random baseline, data loader, and visualization modules.
- `main.py`: Main script to run the bandit simulation and comparison.

## Outputs
- **Cumulative Reward Comparison**: Compares Thompson Sampling vs. Random Selection.
- **Conversion Rate per Arm**: Shows how effective each arm (ad position) was.

## Notes
- The project uses the `ad_position` column as the arm.
- Reward is 1 if a click occurred on the selected ad, 0 otherwise.
- Preprocessing includes filling missing values and label/one-hot encoding.

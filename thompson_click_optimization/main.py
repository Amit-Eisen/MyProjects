import os
from src.data_preprocessing import preprocess_data
from src.data_loader import load_data
from src.thompson_sampler import ThompsonSampler
from src.baseline_random import RandomSelector
from src.visualizer import (
    plot_arm_selection,
    plot_comparison,
    print_conversion_rates
)

def main():
    raw_path = "data/ad_click_dataset.csv"
    processed_path = "data/processed_data.csv"

    if not os.path.exists(processed_path):
        print("[INFO] Processed data not found. Preprocessing now...")
        preprocess_data(raw_path, processed_path)
    else:
        print("[INFO] Using existing processed data.")

    df = load_data(processed_path)
    num_arms = df['arm'].nunique()

    # Thompson Sampling
    ts = ThompsonSampler(num_arms)
    ts_choices, ts_rewards = [], []
    for _, row in df.iterrows():
        arm = ts.select_arm()
        reward = 1 if row['click'] == 1 and row['arm'] == arm else 0
        ts.update(arm, reward)
        ts_choices.append(arm)
        ts_rewards.append(reward)

    # Random Selection
    rs = RandomSelector(num_arms)
    rs_choices, rs_rewards = [], []
    for _, row in df.iterrows():
        arm = rs.select_arm()
        reward = 1 if row['click'] == 1 and row['arm'] == arm else 0
        rs.update(arm, reward)
        rs_choices.append(arm)
        rs_rewards.append(reward)

    # Visualizations
    plot_comparison(ts_rewards, rs_rewards)
    print_conversion_rates(ts_choices, ts_rewards)

if __name__ == "__main__":
    main()

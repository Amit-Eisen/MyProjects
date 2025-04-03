import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_arm_selection(arm_choices, num_arms):
    plt.figure(figsize=(8, 5))
    plt.hist(arm_choices, bins=num_arms, edgecolor='black')
    plt.title('Histogram of arm selections')
    plt.xlabel('Arm index')
    plt.ylabel('Number of times selected')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_cumulative_reward(rewards, label):
    cumulative_rewards = np.cumsum(rewards)
    plt.plot(cumulative_rewards, label=label)


def plot_comparison(thompson_rewards, random_rewards):
    plt.figure(figsize=(8, 5))
    plot_cumulative_reward(thompson_rewards, "Thompson Sampling")
    plot_cumulative_reward(random_rewards, "Random Selection")
    plt.title("Cumulative Reward Comparison")
    plt.xlabel("Round")
    plt.ylabel("Cumulative Reward")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def print_conversion_rates(choices, rewards):
    df = pd.DataFrame({'arm': choices, 'reward': rewards})
    summary = df.groupby('arm')['reward'].agg(['count', 'sum'])
    summary['conversion_rate'] = summary['sum'] / summary['count']
    print("\nConversion Rate per Arm:\n")
    print(summary)

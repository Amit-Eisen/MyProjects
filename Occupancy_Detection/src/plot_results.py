import matplotlib.pyplot as plt
import numpy as np

def plot_accuracies(num_samples, accuracies):
    """Plots accuracy of classifiers as a function of training sample size."""
    plt.figure(figsize=(10, 6))
    for clf_name, acc_values in accuracies.items():
        plt.plot(num_samples, np.array(acc_values) * 100, label=clf_name)
    plt.title("Success Rate (%) vs Number of Training Samples")
    plt.xlabel("Number of Training Samples")
    plt.ylabel("Success Rate (%)")
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(True)
    plt.show()

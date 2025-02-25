import matplotlib.pyplot as plt

def plot_results(x_t, f_history, v_history, distance_history, car_1_x, car_2_x, passing_time):
    """
    Plot the results of the simulation.
    """
    fig, (ax3, ax4, ax5, ax6) = plt.subplots(ncols=4, figsize=(12, 3.5))

    ax3.plot(x_t, f_history)
    ax3.plot([passing_time, passing_time], [-1500, 3000], ':k')
    ax3.set_title("F(t)")
    ax3.set_ylabel('F (N)')
    ax3.set_xlabel('Time (s)')

    ax4.plot(x_t, v_history)
    ax4.set_title("Velocity of car 1 (t)")
    ax4.set_ylabel('V (m/s)')
    ax4.set_xlabel('Time (s)')

    ax5.plot(x_t, distance_history)
    ax5.plot([passing_time, passing_time], [0, 25], ':k')
    ax5.set_title("Distance between cars (t)")
    ax5.set_ylabel('Distance (m)')
    ax5.set_xlabel('Time (s)')

    ax6.plot(x_t, car_1_x, 'b', label='Car 1')
    ax6.plot(x_t, car_2_x, 'r', label='Car 2')
    ax6.plot([passing_time, passing_time], [0, 100], ':k')
    ax6.set_title("Car Positions (t)")
    ax6.set_ylabel('X (m)')
    ax6.set_xlabel('Time (s)')
    ax6.legend(loc='upper left')

    plt.tight_layout()
    plt.show()

from two_cars import two_cars
from fuzzy_control import compute_fuzzy_force
from visualization import plot_results
from constants import y0_input, Tf

# Initialize simulation variables
f_history, v_history, distance_history = [], [], []
car_1_x, car_2_x, x_t = [], [], []
passing_time = None

Cars = two_cars(y0=y0_input)
f_cog = 0
i = 0

# Run simulation loop
while Cars.x < Cars.road_Length and Cars.t < Tf:
    print(f'Time: {round(Cars.t, 2)} sec, Position: {round(Cars.x, 2)} m, distance: {round(Cars.distance, 2)} m')

    success = Cars.step(f=f_cog)
    if not success:
        break

    f_cog = compute_fuzzy_force(Cars.distance, Cars.v)

    f_history.append(f_cog)
    v_history.append(Cars.v)
    distance_history.append(Cars.distance)
    x_t.append(Cars.t)
    car_1_x.append(Cars.x)
    car_2_x.append(Cars.x_lead)

    if Cars.x >= 50 and passing_time is None:
        passing_time = Cars.t

    if i % 50 == 0:
        Cars.draw()

    i += 1

plot_results(x_t, f_history, v_history, distance_history, car_1_x, car_2_x, passing_time)

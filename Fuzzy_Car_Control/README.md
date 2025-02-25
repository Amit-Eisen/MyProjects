# Fuzzy Logic Car Distance Control

This project implements a fuzzy logic–based controller for maintaining a safe distance between two cars. The project uses a provided simulation module (`two_cars.py`, supplied by the instructor) to model the car dynamics, and a custom fuzzy controller (`fuzzy_control.py`) to compute the control signal based on sensor inputs (e.g., distance, speed).

## Project Structure
````
Fuzzy_Car_Control/ 
├── src/ │
 ├── two_cars.py # Provided simulation code (DO NOT MODIFY) │ 
 ├── fuzzy_control.py # Custom fuzzy logic controller implementation │
 ├── visualization.py # Functions to visualize simulation results │ 
 ├── constants.py # Project constants and configuration │
 └── main.py # Main script to run the simulation 
├── README.md # This file 
└── requirements.txt # Required Python libraries
````

## Overview

The objective of this project is to demonstrate how fuzzy logic can be applied to control the distance between two vehicles in a dynamic simulation. The provided simulation models the motion of a lead car and a following car. Our fuzzy controller computes a control force based on the measured distance and other parameters to maintain a safe following distance.

The project compares the performance of the fuzzy controller with the baseline simulation and displays results via real-time visualizations and performance metrics.

## How to Run

1. **Install Dependencies**

   Ensure you have Python 3 installed, then run:
   ```bash
   pip install -r requirements.txt

2. **Run the Simulation:**

   python src/main.py

## Results

   **Real-Time Visualization:**
   The simulation displays the positions of both cars and shows a plot of the control signal and other parameters over time.
   Performance Metrics: The terminal outputs metrics such as current time, car positions, distance between cars, and any collision warnings.

## Future Improvements
   **Fuzzy Controller Tuning:**

   Further tuning of membership functions and fuzzy rules could enhance performance.
   Data-Driven Optimization: Future work could use optimization methods (e.g., genetic algorithms) to automatically fine-tune the fuzzy parameters.
   Extended Scenarios: The simulation environment can be extended to more complex driving scenarios or to incorporate sensor noise.

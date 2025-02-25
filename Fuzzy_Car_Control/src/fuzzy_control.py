import numpy as np
import skfuzzy as fuzz
from constants import x_f, x_distance, x_velocity

def define_fuzzy_sets():
    """
    Define fuzzy sets for distance, velocity, and force.
    """
    distance_sets = {
        "near": fuzz.gaussmf(x_distance, 4, 2),
        "good": fuzz.gaussmf(x_distance, 8, 1.25),
        "far": fuzz.gaussmf(x_distance, 15, 2.75),
        "very_far": fuzz.gaussmf(x_distance, 18, 5)
    }

    velocity_sets = {
        "slow": fuzz.trimf(x_velocity, [0, 0, 2.5]),
        "mid": fuzz.trimf(x_velocity, [2, 3, 5]),
        "fast": fuzz.trimf(x_velocity, [3.5, 10, 10])
    }

    force_sets = {
        "low": fuzz.trimf(x_f, [-1500, -1500, 0]),
        "mid": fuzz.trimf(x_f, [-500, 0, 1500]),
        "high": fuzz.trimf(x_f, [0, 3000, 3000])
    }

    return distance_sets, velocity_sets, force_sets

def compute_fuzzy_force(distance, velocity):
    """
    Compute the force using fuzzy logic rules.
    """
    distance_sets, velocity_sets, force_sets = define_fuzzy_sets()

    distance_levels = {key: fuzz.interp_membership(x_distance, value, distance) for key, value in distance_sets.items()}
    velocity_levels = {key: fuzz.interp_membership(x_velocity, value, velocity) for key, value in velocity_sets.items()}

    # Rule #1: If the distance is far OR velocity is slow → Apply high force
    alpha1 = np.fmax(distance_levels["far"], velocity_levels["slow"])
    f_activation_lo = np.fmin(alpha1, force_sets["high"])

    # Rule #2: If the velocity is fast → Apply low force
    alpha2 = velocity_levels["fast"]
    f_activation_mid = np.fmin(alpha2, force_sets["low"])

    # Rule #3: If the distance is good AND velocity is steady → Apply medium force
    alpha3 = np.fmin(distance_levels["good"], velocity_levels["mid"])
    f_activation_hi = np.fmin(alpha3, force_sets["mid"])

    # Rule #4: If the distance is very far AND velocity is slow → Apply high force
    alpha4 = np.fmin(distance_levels["very_far"], velocity_levels["slow"])
    f_activation_ = np.fmin(alpha4, force_sets["high"])

    # Aggregate all the fuzzy sets
    beta = np.fmax(f_activation_lo, np.fmax(f_activation_mid, f_activation_hi))

    # Defuzzification to get a crisp output force value
    return fuzz.defuzz(x_f, beta, 'som')

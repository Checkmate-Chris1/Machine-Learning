""" Machine Learning with scikit-learn and user input

    This works similar to example.py but has customizable data set by the user when ran
"""

import numpy as np

# Initialize weights and bias
weight = np.random.uniform(-1, 1)  # Start with random weight
bias = np.random.uniform(-1, 1)    # Start with random bias
learning_rate = 0.01

# Reward function: based on error
def reward_function(true, predicted):
    return -abs(true - predicted)  # Negative reward for higher error

# Training loop (Reinforcement Learning)
for _ in range(5000):  # Number of episodes
    x = np.random.randint(1, 21)  # Random input
    true_output = 2*x        # True formula

    # Predict using the current weight and bias
    predicted_output = weight * x + bias

    # Compute reward
    reward = reward_function(true_output, predicted_output)

    # Update weights and bias (gradient descent-like approach)
    weight += learning_rate * (true_output - predicted_output) * x
    bias += learning_rate * (true_output - predicted_output)

# Test the learned model
while True:
    user_input = input("Enter a number to test (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    x = int(user_input)
    predicted_output = weight * x + bias
    print(f"Predicted output for {x}: {predicted_output}")

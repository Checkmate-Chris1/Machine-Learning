import tensorflow as tf
import numpy as np

# Generate some data: x and y = x^2
X = np.linspace(-10, 10, 100).reshape(-1, 1)
y = X**2

# Create a simple neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, input_dim=1, activation='relu'),  # Hidden layer with ReLU activation
    tf.keras.layers.Dense(1)  # Output layer (linear activation by default)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X, y, epochs=1000, verbose=0)

# Make predictions
y_pred = model.predict(X)

# Display the first 10 predictions and corresponding true values
print("x \t True y \t Predicted y")
for i in range(10):
    print(f"{X[i][0]:.2f} \t {y[i][0]:.2f} \t\t {y_pred[i][0]:.2f}")

# Print a prediction for a specific input
x_test = np.array([[5]])
y_test_pred = model.predict(x_test)
print(f"\nPrediction for x=5: {y_test_pred[0][0]:.2f}")

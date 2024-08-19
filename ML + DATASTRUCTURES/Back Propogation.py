import numpy as np

# Define the sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Generate some example data
np.random.seed(0)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Initialize weights and biases
input_layer_size = 2
hidden_layer_size = 4
output_layer_size = 1

weights_input_hidden = np.random.uniform(-1, 1, (input_layer_size, hidden_layer_size))
weights_hidden_output = np.random.uniform(-1, 1, (hidden_layer_size, output_layer_size))
bias_hidden = np.random.uniform(-1, 1, (1, hidden_layer_size))
bias_output = np.random.uniform(-1, 1, (1, output_layer_size))

learning_rate = 0.1
epochs = 10000

# Training loop
for epoch in range(epochs):
    # Forward pass
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    output_layer_output = sigmoid(output_layer_input)
    
    # Compute the loss (mean squared error)
    loss = np.mean((y - output_layer_output) ** 2)
    
    # Backward pass
    output_layer_error = y - output_layer_output
    output_layer_delta = output_layer_error * sigmoid_derivative(output_layer_output)
    
    hidden_layer_error = np.dot(output_layer_delta, weights_hidden_output.T)
    hidden_layer_delta = hidden_layer_error * sigmoid_derivative(hidden_layer_output)
    
    # Update weights and biases
    weights_hidden_output += np.dot(hidden_layer_output.T, output_layer_delta) * learning_rate
    weights_input_hidden += np.dot(X.T, hidden_layer_delta) * learning_rate
    bias_output += np.sum(output_layer_delta, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(hidden_layer_delta, axis=0, keepdims=True) * learning_rate
    
    if epoch % 1000 == 0:
        print(f'Epoch {epoch}, Loss: {loss:.4f}')

# Final output after training
print("Final predictions:")
print(output_layer_output)

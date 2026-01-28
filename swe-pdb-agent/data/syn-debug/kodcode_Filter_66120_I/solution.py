import numpy as np

def sigmoid(x):
    """
    Sigmoid activation function
    """
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """
    Derivative of the sigmoid function
    """
    return x * (1 - x)

class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_layer_size, output_size):
        # Initialize weights with random values
        self.input_size = input_size
        self.hidden_layer_size = hidden_layer_size
        self.output_size = output_size

        self.weights_input_hidden = np.random.rand(self.hidden_layer_size, self.input_size)
        self.weights_hidden_output = np.random.rand(self.output_size, self.hidden_layer_size)

    def feedforward(self, X):
        """
        Perform a feedforward computation.
        """
        self.hidden_layer_input = np.dot(X, self.weights_input_hidden)
        self.hidden_layer_output = sigmoid(self.hidden_layer_input)

        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output)
        self.output = sigmoid(self.output_layer_input)
        
        return self.output

    def backpropagate(self, X, y, learning_rate):
        """
        Perform backpropagation and update weights.
        """
        # Feedforward
        self.feedforward(X)

        # Calculate error
        error = y - self.output
        
        # Derivatives for output and hidden layers
        d_output = error * sigmoid_derivative(self.output)
        error_hidden_layer = d_output.dot(self.weights_hidden_output.T)
        d_hidden_layer = error_hidden_layer * sigmoid_derivative(self.hidden_layer_output)

        # Update weights
        self.weights_hidden_output += self.output.T.dot(d_output) * learning_rate
        self.weights_input_hidden += self.output.T.dot(d_hidden_layer) * learning_rate

    def train(self, X, y, epochs, learning_rate):
        """
        Train the neural network over a number of epochs.
        """
        for epoch in range(epochs):
            self.backpropagate(X, y, learning_rate)

    def predict(self, X):
        """
        Make a prediction for input X.
        """
        return self.feedforward(X)

# Example of usage:
# Create a neural network with 2 input neurons, 3 hidden neurons, and 1 output neuron
# nn = SimpleNeuralNetwork(input_size=2, hidden_layer_size=3, output_size=1)

# Example training data
# X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# y = np.array([[0], [1], [1], [0]])

# Train the neural network
# nn.train(X, y, epochs=10000, learning_rate=0.1)
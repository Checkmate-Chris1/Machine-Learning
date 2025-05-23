"""
This is a workspace to follow directions that come from the YouTube playlist "Neural Networks from Scratch"
Link: https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=1
"""
import numpy as np


class Neuron:
    def __init__(self, weights: list[float], bias: int = 0):
        self.weights = weights
        self.bias = bias

    def ReLU(self, inputs):
        return np.maximum(0, inputs)

    def predict(self, inputs) -> int:
        '''
        Calculates an output using the neuron's weights, biases, and provided inputs
        :param inputs: The values used with the weights and biases
        :return: Output
        '''
        return np.dot(self.weights, inputs) + self.bias

def main():
    inputs = [[1, 2, 3, 2.5],
              [2.0, 5.0 - 1.0, 2.0],
              [-1.5, 2.7, 3.3, -0.8]]
    weights = [[0.2, 0.8, -0.5, 1.0],
               [0.5, -0.91, 0.26, -0.5],
               [-0.26, -0.27, 0.17, 0.87]]
    biases = [2, 3, 0.5]

    neuron = Neuron(weights[0], biases[0])
    neuron2 = Neuron(weights[1], biases[1])
    neuron3 = Neuron(weights[2], biases[2])

    print(neuron.predict(inputs))
    print(neuron2.predict(inputs))
    print(neuron3.predict(inputs))

if __name__ == "__main__":
    main()
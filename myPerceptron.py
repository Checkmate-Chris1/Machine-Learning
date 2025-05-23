class Perceptron:
    def __init__(self, learning_rate: float = 0.01, weight: float = 0.0, bias: float = 0.0):
        self.learning_rate = learning_rate
        self.weight = weight
        self.bias = bias

    def calculate_error(self, y_predicted: float, y_actual: float) -> float:
        """
        Finds the difference between the guessed number and the actual number
        :param y_predicted: Predicted output
        :param y_actual: Actual output
        :return: Error; positive if too low, negative if too high
        """
        return y_actual - y_predicted

    def predict(self, X: int) -> float:
        """
        Predicts the output for a given input
        :param X: number
        :return: Predicted output number
        """
        return X * self.weight + self.bias

    def train(self, X: int, y: float) -> None:
        """
        Train the model with one set of data
        :param X: Input number
        :param y: Expected output number
        :return: None
        """
        y_predicted = self.predict(X)
        error = self.calculate_error(y_predicted, y)
        self.weight += self.learning_rate * error * X
        self.bias += self.learning_rate * error


def main():
    model = Perceptron(0.01, 1, 1)
    for i in range(1000):
        for i in range(10):
            model.train(i, (i * 3) + 2)
    print("Learning Rate:", model.learning_rate)
    print("Weight:", model.weight)
    print("Bias:", model.bias)
    print(model.predict(100))


if __name__ == "__main__":
    main()

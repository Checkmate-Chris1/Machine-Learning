"""
Machine Learning using a Perceptron-based Polynomial Regression system

Should be able to predict any function up to the fourth exponent after training for a bit.
ChatGPT added tkinter GUI showing the progress of its weight variables
"""

from PerceptronDataSummaryGui import DataGui
import tkinter as tk

class Perceptron:
    def __init__(self, learning_rate: float = 0.01, weight: float = 0.0, weight2: float = 0.0, weight3: float = 0.0,
                 weight4: float = 0.0, bias: float = 0.0):
        self.learning_rate = learning_rate
        self.weight = weight
        self.weight2 = weight2
        self.weight3 = weight3
        self.weight4 = weight4
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
        return ((X ** 4 * self.weight4) + (X ** 3 * self.weight3) + (X ** 2 * self.weight2) +
                (X * self.weight) + self.bias)

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
        self.weight2 += (self.learning_rate/10) * error * X ** 2
        self.weight3 += (self.learning_rate/100) * error * X ** 3
        self.weight4 += (self.learning_rate/1000) * error * X ** 4
        self.bias += self.learning_rate * error

def main():
    # Options
    trains_per_update = 1
    total_trains = 10000000000
    update_rate = 10
    visual_multiplier = 50 # Make numbers bigger to see

    def training_formula(x: int) -> float:
        """
        The formula that determines the expected output, used for training model
        :param x: Input
        :return: Expected output
        """
        return x**3
    # Options END

    model = Perceptron(0.00001)
    global current_trains
    current_trains = 0

    def train_loop(train_times):
        global current_trains
        current_trains += trains_per_update
        for _ in range(train_times):
            for i in range(-10, 10):
                model.train(i, training_formula(i))
        gui.length1 = model.weight * visual_multiplier # Setting rectangle lengths
        gui.length2 = model.weight2 * visual_multiplier
        gui.length3 = model.weight3 * visual_multiplier
        gui.length4 = model.weight4 * visual_multiplier
        gui.length5 = model.bias * visual_multiplier
        gui.draw_rectangles(visual_multiplier)  # I got lazy with this, and now I have to pass the visual
                                                # multiplier to calculate rectangle size
        if current_trains < total_trains: # Keep looping if not done
            root.after(update_rate, train_loop, trains_per_update)

    # print("Learning Rate:", model.learning_rate)
    # print("Weight:", model.weight)
    # print("Bias:", model.bias)
    # print(model.predict(5))

    root = tk.Tk()
    gui = DataGui(root, 10, 10, 10, 10, 10)
    root.title("Summary of Perceptron Data")
    train_loop(0)
    root.mainloop()

    print("Actual:", training_formula(-5))
    print("Predicted:",model.predict(-5))


if __name__ == "__main__":
    main()

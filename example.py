""" Machine Learning with scikit-learn

    This is an example project showcasing a basic application of scikit-learn
    For a given input of one number, the output should be that number
    The model is trained with some data, then tested with
"""

import sklearn as sk
import sklearn.linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Training data (both for training and testing)
X = [[1], [2], [3], [4], [5]]
y = [1, 2, 3, 4, 5]

# This splits the data into training and testing sets, to test the model on different information from the training data
# In this case, I give 5 samples of data, and the test size is 0.2 (20%) of the total data, so there will only be 1 test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initiating and training model
model = LinearRegression()
model.fit(X_train, y_train)

# Results from model prediction
print("Input: " + str(X_test))
print("Prediction: " + str(model.predict(X_test)))
print("Actual: " + str(y_test))
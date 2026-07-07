import numpy as np

#1- Creating a class for logistic regression
class LogisticRegression:
    def __init__(self, iterations, lr):
        self.lr = lr
        self.iterations = iterations
        self.w = None
        self.b= None
        self.costs = []

#2- Implementing tje sigmoid function
    def sigmoid(self, z):
        return 1/(1+np.exp(-z))

#3- Initializing random parameters
    def initialize_parameters(self, n_features):
        np.random.seed(1)
        self.w = np.random.randn(n_features, 1) * 0.1
        self.b = 0.0

#4- Applying the sigmoid function
    def forward_propagation(self, X):
        z = np.dot(X, self.w) + self.b
        return self.sigmoid(z)

#5- Calculating the cost function BCE
    def compute_cost(self, y, h):
        m = y.shape[0]
        epsilon = 1e-7
        h = np.clip(h, epsilon, 1-epsilon)
        cost = -(1 / m) * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
        return cost

#6- Calculating the gradients
    def compute_gradient(self, X, y, h):
        m = y.shape[0]
        dw = np.dot(X.T, h - y) / m
        db = np.mean(h - y)
        return dw, db

#7- Implementing the training/fitting method
    def fit(self, X_train, y_train):
        self.initialize_parameters(X_train.shape[1])
        for i in range(self.iterations):
            h = self.forward_propagation(X_train)
            cost = self.compute_cost(y_train, h)
            dw, db = self.compute_gradient(X_train, y_train, h)
            self.w -= self.lr * dw
            self.b -= self.lr * db
            self.costs.append(cost)
            if i % 200 == 0:
                print(f"Iteration: {i:.2f} \n cost: {cost:.2f}")

#8- Implementing the prediction method
    def predict(self, X_test):
        probabilities = self.forward_propagation(X_test)
        return (probabilities >= 0.5).astype(int)

#9- Implementing the testing method
    def evaluate(self, X_test, y_test):
        predictions = self.predict(X_test)
        accuracy = np.mean(predictions == y_test)*100
        return accuracy



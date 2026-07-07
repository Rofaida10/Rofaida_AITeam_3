import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from classification import LogisticRegression




def load_dataset(file_name):
    #shuffle dataset to avoid bias
    data = pd.read_csv(file_name)
    data = data.sample(frac=1, random_state=42).reset_index(drop=True)
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values.reshape(-1, 1)
    return X, y

def split_train_test(X, y, train_size=0.8):
    split_index = int(len(X) * train_size)
    X_train, X_test = X[:split_index], X[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]
    return X_train, X_test, y_train, y_test

def main():
    file_name = "xor4.csv"

#load dataset
    X, y = load_dataset(file_name)

#split dataset to train and test
    X_train, X_test, y_train, y_test = split_train_test(X, y)

#create logistic regression
    model = LogisticRegression(lr= 0.01, iterations=1000)
#train the model
    model.fit(X_train, y_train)

#make predictions
    predictions = model.predict(X_test)

#evaluate model accuracy
    accuracy = model.evaluate(X_test, y_test)

    print("Predictions: ", predictions)
    print("Actual labels: ", y_test)
    print(f"Accuracy: {accuracy:.2f}%")
    print("Weights: ", model.w)
    print("Bias: ", model.b)

#Display Loss
    plt.figure(figsize=(12, 8))
    plt.plot(model.costs)
    plt.xlabel("Iterations")
    plt.ylabel("Binary Cross Entropy Loss BCE")
    plt.title("Training Loss")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()


import numpy as np

X=np.array([50, 60, 80, 100, 120])
y=np.array([150, 180, 240, 300, 330])

X=X.reshape((-1,1))
ones=np.ones((X.shape[0],1))
X_b=np.hstack((ones,X))
θ= np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
print("Theta values are:\n",θ)

#predict the price of a 90 m² house
X_new=np.array([1,90])
prediction=X_new @ θ
print("\nPredicted price for 90 m² house: ",prediction)



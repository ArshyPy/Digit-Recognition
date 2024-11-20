import numpy as np 

def loadData():
    X = np.load("data sets/X.npy")
    Y = np.load("data sets/y.npy")
    X = X[0:5000]
    Y = Y[0:5000]
    return X, Y
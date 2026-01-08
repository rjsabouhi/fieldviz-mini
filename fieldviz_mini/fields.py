import numpy as np

class VectorField:
    def __init__(self, func):
        """
        func: callable (x, y) -> (dx, dy)
        """
        self.func = func

    def evaluate(self, X, Y):
        FX = np.zeros_like(X)
        FY = np.zeros_like(Y)
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                fx, fy = self.func(X[i, j], Y[i, j])
                FX[i, j] = fx
                FY[i, j] = fy
        return FX, FY

import numpy as np
from .fields import VectorField

def spiral_sink(a=0.5, b=1.0):
    def f(x, y):
        return -a*x - b*y, b*x - a*y
    return VectorField(f)

def saddle_point():
    def f(x, y):
        return x, -y
    return VectorField(f)

def lorenz_field(sigma=10, beta=8/3, rho=28):
    def f(x, y):
        dx = sigma * (y - x)
        dy = x * (rho - y) - x
        return dx, dy
    return VectorField(f)

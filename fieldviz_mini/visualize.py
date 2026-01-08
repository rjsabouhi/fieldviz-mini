import numpy as np
import matplotlib.pyplot as plt

def plot_vector_field(field, xlim=(-2,2), ylim=(-2,2), density=20):
    x = np.linspace(*xlim, density)
    y = np.linspace(*ylim, density)
    X, Y = np.meshgrid(x, y)
    FX, FY = field.evaluate(X, Y)

    plt.figure(figsize=(6,6))
    plt.quiver(X, Y, FX, FY, color="black", alpha=0.6)
    plt.title("Vector Field")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.show()

def plot_streamlines(field, seeds, steps=500, dt=0.01):
    from .integrators import integrate_streamline

    plt.figure(figsize=(6,6))
    for (x0, y0) in seeds:
        traj = integrate_streamline(field, x0, y0, steps=steps, dt=dt)
        plt.plot(traj[:,0], traj[:,1], linewidth=1)

    plt.title("Streamlines")
    plt.axis("equal")
    plt.show()

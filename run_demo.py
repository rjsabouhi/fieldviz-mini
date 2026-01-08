import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fieldviz_mini import spiral_sink, saddle_point, lorenz_field
from fieldviz_mini.integrators import integrate_streamline

def plot_vector_field_save(field, filename, xlim=(-2,2), ylim=(-2,2), density=20, title="Vector Field"):
    x = np.linspace(*xlim, density)
    y = np.linspace(*ylim, density)
    X, Y = np.meshgrid(x, y)
    FX, FY = field.evaluate(X, Y)

    plt.figure(figsize=(6,6))
    plt.quiver(X, Y, FX, FY, color="black", alpha=0.6)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filename}")

def plot_streamlines_save(field, seeds, filename, steps=500, dt=0.01, title="Streamlines"):
    plt.figure(figsize=(6,6))
    for (x0, y0) in seeds:
        traj = integrate_streamline(field, x0, y0, steps=steps, dt=dt)
        plt.plot(traj[:,0], traj[:,1], linewidth=1)
    plt.title(title)
    plt.axis("equal")
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filename}")

print("=== fieldviz-mini Demo ===\n")

field = spiral_sink()
plot_vector_field_save(field, "output_spiral_field.png", title="Spiral Sink - Vector Field")
plot_streamlines_save(field, seeds=[(1,1), (-1,0), (0.5,-1), (1.5, 0.5)], filename="output_spiral_streamlines.png", title="Spiral Sink - Streamlines")

field2 = saddle_point()
plot_vector_field_save(field2, "output_saddle_field.png", title="Saddle Point - Vector Field")
plot_streamlines_save(field2, seeds=[(0.5, 0.1), (-0.5, 0.1), (0.1, 0.5), (0.1, -0.5)], filename="output_saddle_streamlines.png", title="Saddle Point - Streamlines", steps=100)

print("\nDemo complete! Check output_*.png files.")
print("\nPackage ready for export and PyPI publishing.")

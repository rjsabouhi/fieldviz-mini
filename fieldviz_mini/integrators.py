import numpy as np

def euler_step(field, x, y, dt=0.01):
    dx, dy = field.func(x, y)
    return x + dt*dx, y + dt*dy

def rk4_step(field, x, y, dt=0.01):
    f = field.func
    k1 = f(x, y)
    k2 = f(x + dt*k1[0]/2, y + dt*k1[1]/2)
    k3 = f(x + dt*k2[0]/2, y + dt*k2[1]/2)
    k4 = f(x + dt*k3[0],   y + dt*k3[1])
    dx = (k1[0] + 2*k2[0] + 2*k3[0] + k4[0]) / 6
    dy = (k1[1] + 2*k2[1] + 2*k3[1] + k4[1]) / 6
    return x + dt*dx, y + dt*dy

def integrate_streamline(field, x0, y0, steps=1000, dt=0.01, method="rk4"):
    x, y = x0, y0
    traj = [(x, y)]
    step_func = rk4_step if method=="rk4" else euler_step

    for _ in range(steps):
        x, y = step_func(field, x, y, dt=dt)
        traj.append((x, y))
    return np.array(traj)

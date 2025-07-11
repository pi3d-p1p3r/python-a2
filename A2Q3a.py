import numpy as np
import matplotlib.pyplot as plt

def derivatives_curve1(t):
    e_t = np.exp(t)
    r_p = np.array([e_t, e_t * (np.cos(t) - np.sin(t)), e_t * (np.sin(t) + np.cos(t))])
    r_pp = np.array([e_t, e_t * (-2 * np.sin(t)), e_t * (2 * np.cos(t))])
    return r_p, r_pp

def derivatives_curve2(t):
    r_p = np.array([-2 * np.sin(t), 3 * np.cos(t), 0])
    r_pp = np.array([-2 * np.cos(t), -3 * np.sin(t), 0])
    return r_p, r_pp

def curvature(r_p, r_pp):
    cross = np.cross(r_p, r_pp)
    return np.linalg.norm(cross) / (np.linalg.norm(r_p)**3)

# Parameter range
t = np.linspace(0, 2*np.pi, 1000)

# Calculate curvature for both curves
kappa1 = [curvature(*derivatives_curve1(ti)) for ti in t]
kappa2 = [curvature(*derivatives_curve2(ti)) for ti in t]

# Plot individual curves
plt.figure(figsize=(10, 6))
plt.plot(t, kappa1, label='Curve 1', linewidth=2)
plt.title('Curvature (κ) vs t for Curve 1')
plt.xlabel('t')
plt.ylabel('κ')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(t, kappa2, label='Curve 2', linewidth=2)
plt.title('Curvature (κ) vs t for Curve 2')
plt.xlabel('t')
plt.ylabel('κ')
plt.grid(True)
plt.show()

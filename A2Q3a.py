import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def curve1_derivatives(t):
    # r(t) = e^t i + e^t cos(t) j + e^t sin(t) k
    # First derivatives
    x_prime = np.exp(t)
    y_prime = np.exp(t) * (np.cos(t) - np.sin(t))
    z_prime = np.exp(t) * (np.sin(t) + np.cos(t))
    
    # Second derivatives
    x_double_prime = np.exp(t)
    y_double_prime = np.exp(t) * (-2*np.sin(t))
    z_double_prime = np.exp(t) * (2*np.cos(t))
    
    return np.array([x_prime, y_prime, z_prime]), np.array([x_double_prime, y_double_prime, z_double_prime])

def curve2_derivatives(t):
    # r(t) = 2cos(t)i + 3sin(t)j
    # First derivatives
    x_prime = -2 * np.sin(t)
    y_prime = 3 * np.cos(t)
    z_prime = 0
    
    # Second derivatives
    x_double_prime = -2 * np.cos(t)
    y_double_prime = -3 * np.sin(t)
    z_double_prime = 0
    
    return np.array([x_prime, y_prime, z_prime]), np.array([x_double_prime, y_double_prime, z_double_prime])

def compute_TNB(r_prime, r_double_prime):
    # Tangent vector
    T = r_prime / np.linalg.norm(r_prime)
    
    # Binormal vector
    B = np.cross(r_prime, r_double_prime)
    B = B / np.linalg.norm(B)
    
    # Normal vector
    N = np.cross(B, T)
    
    return T, N, B

def compute_curvature(r_prime, r_double_prime):
    cross_prod = np.cross(r_prime, r_double_prime)
    return np.linalg.norm(cross_prod) / (np.linalg.norm(r_prime)**3)

def compute_torsion(r_prime, r_double_prime, r_triple_prime):
    cross_prod = np.cross(r_prime, r_double_prime)
    if np.linalg.norm(cross_prod) == 0:
        return 0
    return np.dot(cross_prod, r_triple_prime) / (np.linalg.norm(cross_prod)**2)

t = np.linspace(0, 2*np.pi, 1000)

# For curve 1
print("Curve 1 at t=0:")
r_prime, r_double_prime = curve1_derivatives(0)
T, N, B = compute_TNB(r_prime, r_double_prime)

kappa_values1 = []
for t_val in t:
    r_prime, r_double_prime = curve1_derivatives(t_val)
    kappa1 = compute_curvature(r_prime, r_double_prime)
    kappa_values1.append(kappa1)
print(f"T={T}, N={N}, B={B}, κ={kappa1}")

plt.figure(figsize=(10, 6))
plt.plot(t, kappa_values1)
plt.title('Curvature (κ) vs t for Curve 1')
plt.xlabel('t')
plt.ylabel('κ')
plt.grid(True)
plt.show()

# For curve 2
print("\nCurve 2:")
kappa_values2 = []
for t_val in t:
    r_prime, r_double_prime = curve2_derivatives(t_val)
    kappa = compute_curvature(r_prime, r_double_prime)
    kappa_values2.append(kappa)

plt.figure(figsize=(10, 6))
plt.plot(t, kappa_values2)
plt.title('Curvature (κ) vs t for Curve 2')
plt.xlabel('t')
plt.ylabel('κ')
plt.grid(True)
plt.show()

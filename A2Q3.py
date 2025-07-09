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

# Part (b) - Laplace and Cauchy-Riemann equations
def verify_laplace(x, y):
    # f(x,y) = y^2 cos(x-y)
    # Computing second partial derivatives
    fxx = lambda x, y: -y**2 * np.cos(x-y)
    fyy = lambda x, y: 2*np.cos(x-y) - y**2 * np.cos(x-y) + 4*y*np.sin(x-y)
    
    return fxx(x,y) + fyy(x,y)

def verify_cauchy_riemann(x, y):
    # Computing partial derivatives
    fx = lambda x, y: -y**2 * np.sin(x-y)
    fy = lambda x, y: 2*y*np.cos(x-y) + y**2 * np.sin(x-y)
    
    return fx(x,y), fy(x,y)

# Part (c) - Chain rule
def compute_dw_dtheta(theta):
    x = np.cos(theta)
    y = np.sin(theta)
    z = np.tan(theta)
    
    dw_dx = x / np.sqrt(x**2 + y**2 + z**2)
    dw_dy = y / np.sqrt(x**2 + y**2 + z**2)
    dw_dz = z / np.sqrt(x**2 + y**2 + z**2)
    
    dx_dtheta = -np.sin(theta)
    dy_dtheta = np.cos(theta)
    dz_dtheta = 1 / (np.cos(theta)**2)
    
    return dw_dx * dx_dtheta + dw_dy * dy_dtheta + dw_dz * dz_dtheta

# Part (d) - Gradient and directional derivative
def compute_gradient(x, y):
    # T(x,y) = 3x^2y
    return np.array([6*x*y, 3*x**2])

def compute_directional_derivative(point, direction):
    gradient = compute_gradient(point[0], point[1])
    unit_direction = direction / np.linalg.norm(direction)
    return np.dot(gradient, unit_direction)

def plot_directional_derivative():
    x = np.linspace(-2, 0, 100)
    y = np.linspace(0, 2, 100)
    X, Y = np.meshgrid(x, y)
    
    # Computing directional derivative at each point
    Z = np.zeros_like(X)
    direction = np.array([-1, -0.5])
    
    for i in range(len(x)):
        for j in range(len(y)):
            Z[j,i] = compute_directional_derivative(np.array([X[j,i], Y[j,i]]), direction)
    
    # Creating 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap='viridis')
    plt.colorbar(surf)
    plt.title('Directional Derivative Surface')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


# Part (a)
t = np.linspace(0, 2*np.pi, 1000)

# For curve 1
print("Curve 1 at t=0:")
r_prime, r_double_prime = curve1_derivatives(0)
T, N, B = compute_TNB(r_prime, r_double_prime)
# kappa1 = compute_curvature(r_prime, r_double_prime)

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
kappa_values = []
for t_val in t:
    r_prime, r_double_prime = curve2_derivatives(t_val)
    kappa = compute_curvature(r_prime, r_double_prime)
    kappa_values.append(kappa)

plt.figure(figsize=(10, 6))
plt.plot(t, kappa_values)
plt.title('Curvature (κ) vs t for Curve 2')
plt.xlabel('t')
plt.ylabel('κ')
plt.grid(True)
plt.show()

# Part (b) results
print("\nLaplace equation verification at (1,1):", verify_laplace(1, 1))
fx, fy = verify_cauchy_riemann(1, 1)
print("Cauchy-Riemann equations at (1,1):", fx, fy)

# Part (c) result
print("\ndw/dθ at θ=π/4:", compute_dw_dtheta(np.pi/4))

# Part (d)
point = np.array([-1, 3/2])
direction = np.array([-1, -1/2])
gradient = compute_gradient(point[0], point[1])
dir_deriv = compute_directional_derivative(point, direction)
print(f"\nGradient at (-1, 3/2): {gradient}")
print(f"Directional derivative in direction [-1, -1/2]: {dir_deriv}")

# Plot directional derivative surface
plot_directional_derivative()
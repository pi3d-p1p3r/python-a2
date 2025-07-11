import numpy as np
import matplotlib.pyplot as plt

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

# Part (b) results
print("\nLaplace equation verification at (1,1):", verify_laplace(1, 1))
fx, fy = verify_cauchy_riemann(1, 1)
print("Cauchy-Riemann equations at (1,1):", fx, fy)

# Part (c) result
print("\ndw/dθ at θ=π/4:", compute_dw_dtheta(np.pi/4))

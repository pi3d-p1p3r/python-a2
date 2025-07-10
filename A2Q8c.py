import numpy as np
from scipy.integrate import tplquad

# Vector field F(x,y,z) = x³i + y³j + z²k
# Divergence: ∇·F = 3x² + 3y² + 2z

def divergence(z, y, x):
    """Note: tplquad expects arguments in order (z, y, x)"""
    return 3*x**2 + 3*y**2 + 2*z

# Define the integration limits for the cylindrical region
# x² + y² ≤ 9, 0 ≤ z ≤ 2

# x limits: -3 to 3
x_lower, x_upper = -3, 3

# y limits: functions of x
y_lower = lambda x: -np.sqrt(9 - x**2)
y_upper = lambda x: np.sqrt(9 - x**2)

# z limits: constant functions of x and y
z_lower = lambda x, y: 0
z_upper = lambda x, y: 2

# Perform the triple integral
flux, error = tplquad(divergence, x_lower, x_upper, y_lower, y_upper, z_lower, z_upper)

print(f"Outward flux: {flux}")

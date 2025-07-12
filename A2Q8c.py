import numpy as np
from scipy.integrate import tplquad

# Vector field F(x,y,z) = x³i + y³j + z²k
# Divergence: ∇·F = 3x² + 3y² + 2z
def divergence(z, y, x):
    """Note: tplquad expects arguments in order (z, y, x)"""
    return 3*x**2 + 3*y**2 + 2*z

# Perform the triple integral
flux = tplquad(divergence,                      # expression
                -3, 3,                          # x limits
                lambda x: -np.sqrt(9 - x**2),   # y_upper limit
                lambda x: np.sqrt(9 - x**2),    # y_lower limit
                lambda x, y: 0,                 # z_upper limit
                lambda x, y: 2)                 # z_lower limit

print(f"Outward flux: {flux[0]}")

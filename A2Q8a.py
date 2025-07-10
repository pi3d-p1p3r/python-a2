import numpy as np
from scipy.integrate import dblquad
import matplotlib.pyplot as plt

# Define the components of the force field
P = lambda x, y: np.exp(x) - y**3
Q = lambda x, y: np.cos(y) + x**3

# Calculate partial derivatives
Qx = lambda x, y: 3*x**2        # ∂Q/∂x
Py = lambda x, y: -3*y**2       # ∂P/∂y

# Define the integrand and the limits for the double integral
integrand = lambda y, x: Qx(x, y) - Py(x, y)
lower_y = lambda x: -np.sqrt(1 - x**2)
upper_y = lambda x: np.sqrt(1 - x**2)

# Perform the double integral
work_done = dblquad(integrand, -1, 1, lower_y, upper_y)
print(f"Work done by the force field over the unit disk: {work_done[0]:.10f}")

import numpy as np
from scipy.integrate import quad

# Define the integrand function for the line integral
# (xy + z^3) * ds/dt where ds/dt = |r'(t)|
def integrand(t):
    # Parametric equations
    x = np.cos(t)
    y = np.sin(t) 
    z = t
    
    # Function to integrate: xy + z^3
    f = x * y + z**3
    
    # Calculate ds/dt = |r'(t)|
    # r'(t) = (-sin(t), cos(t), 1)
    # |r'(t)| = sqrt(sin²(t) + cos²(t) + 1) = sqrt(2)
    ds_dt = np.sqrt((-np.sin(t))**2 + (np.cos(t))**2 + 1**2)
    
    return f * ds_dt

# Integration limits
lower_limit = 0
upper_limit = np.pi

# Perform the integration using scipy.integrate.quad
result, error = quad(integrand, lower_limit, upper_limit)

print(f"Line integral result: {result:.10f}")
print(f"Integration error estimate: {error:.2e}")

# Verify the analytical components
print(f"\nVerification:")
print(f"sqrt(2) = {np.sqrt(2):.10f}")
print(f"π⁴/4 = {np.pi**4/4:.10f}")
print(f"sqrt(2) x π⁴/4 = {np.sqrt(2) * np.pi**4/4:.10f}")

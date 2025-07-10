import numpy as np
from scipy.integrate import dblquad

# Define the integrand in spherical coordinates
integrand = lambda phi, theta: (np.sin(phi) * np.cos(theta))**2 * np.sin(phi)

# Integration limits
phi_lower, phi_upper = 0, np.pi              # phi => 0 to pi
theta_lower, theta_upper = 0, 2 * np.pi      # theta => 0 to 2*pi

# Perform the double integral
result, error = dblquad(integrand, theta_lower, theta_upper, lambda theta: phi_lower, lambda theta: phi_upper)

print(f"Result: {result}")

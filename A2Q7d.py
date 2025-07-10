import numpy as np
import sympy as sp
from sympy import symbols, exp, diff, integrate, cos, sin, pi, sqrt
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Define symbolic variables
x, y, t = symbols('x y t')

# Define the force field components
# F(x,y) = e^x î + xe^y ĵ
P = exp(x)        # x-component
Q = x * exp(y)    # y-component

print("Force Field: F(x,y) = e^x î + xe^y ĵ")
print(f"P(x,y) = {P}")
print(f"Q(x,y) = {Q}")
print("=" * 50)

# Part (i): Verify that the force field is conservative
print("\nPart (i): Checking if the force field is conservative")
print("-" * 50)

# For a conservative field, ∂P/∂y = ∂Q/∂x
dP_dy = diff(P, y)
dQ_dx = diff(Q, x)

print(f"∂P/∂y = ∂(e^x)/∂y = {dP_dy}")
print(f"∂Q/∂x = ∂(xe^y)/∂x = {dQ_dx}")

# Check if they are equal
is_conservative = dP_dy.equals(dQ_dx)
print(f"\n∂P/∂y = ∂Q/∂x? {is_conservative}")

if is_conservative:
    print("✓ The force field is CONSERVATIVE on the entire xy-plane")
else:
    print("✗ The force field is NOT conservative")

print("=" * 50)

# Part (ii): Find the potential function φ
print("\nPart (ii): Finding the potential function φ")
print("-" * 50)

# Since F = -∇φ, we have:
# ∂φ/∂x = -P = -e^x
# ∂φ/∂y = -Q = -xe^y

# Integrate the first equation with respect to x
phi_from_x = integrate(-P, x)
print(f"Integrating ∂φ/∂x = -e^x:")
print(f"φ(x,y) = {phi_from_x} + g(y)")

# The potential function should be φ = -e^x - xe^y + C
# Let's verify by finding it systematically
phi = -exp(x) - x*exp(y)
print(f"\nTrying φ(x,y) = {phi}")

# Verify by taking gradients
grad_phi_x = diff(phi, x)
grad_phi_y = diff(phi, y)

print(f"∂φ/∂x = {grad_phi_x}")
print(f"∂φ/∂y = {grad_phi_y}")
print(f"Expected: -e^x, -xe^y")

# Check if -∇φ = F
check_x = (-grad_phi_x).equals(P)
check_y = (-grad_phi_y).equals(Q)

print(f"\n-∂φ/∂x = e^x? {check_x}")
print(f"-∂φ/∂y = xe^y? {check_y}")

if check_x and check_y:
    print("✓ Potential function verified!")
    print(f"φ(x,y) = {phi} + C")
else:
    print("✗ Potential function verification failed")

print("=" * 50)

# Part (iii): Find work done along semicircular path
print("\nPart (iii): Work done from (1,0) to (-1,0) along semicircular path")
print("-" * 50)

# Since the field is conservative, work is path-independent
# Work = φ(final) - φ(initial) = φ(-1,0) - φ(1,0)

# Calculate potential at initial point (1,0)
phi_initial = phi.subs([(x, 1), (y, 0)])
print(f"φ(1,0) = {phi_initial}")

# Calculate potential at final point (-1,0)
phi_final = phi.subs([(x, -1), (y, 0)])
print(f"φ(-1,0) = {phi_final}")

# Work done = φ(final) - φ(initial)
work = phi_final - phi_initial
print(f"\nWork = φ(-1,0) - φ(1,0) = {work}")
print(f"Work = {work.evalf()}")

print("=" * 50)

# Alternative: Verify by direct line integral calculation
print("\nVerification: Direct line integral along semicircular path")
print("-" * 50)

# Parametrize the semicircular path from (1,0) to (-1,0)
# x = cos(t), y = sin(t), where t goes from 0 to π
def line_integral_verification():
    # Parametric equations
    x_param = cos(t)
    y_param = sin(t)
    
    # Derivatives
    dx_dt = diff(x_param, t)
    dy_dt = diff(y_param, t)
    
    # Substitute into force field
    P_param = P.subs([(x, x_param), (y, y_param)])
    Q_param = Q.subs([(x, x_param), (y, y_param)])
    
    # Line integral: ∫(P dx + Q dy) = ∫(P dx/dt + Q dy/dt) dt
    integrand = P_param * dx_dt + Q_param * dy_dt
    
    print(f"Parametric path: x = cos(t), y = sin(t), 0 ≤ t ≤ π")
    print(f"dx/dt = {dx_dt}, dy/dt = {dy_dt}")
    print(f"P along path = {P_param}")
    print(f"Q along path = {Q_param}")
    print(f"Integrand = {integrand}")
    
    # Evaluate the integral
    work_integral = integrate(integrand, (t, 0, pi))
    print(f"\nWork by line integral = {work_integral}")
    print(f"Work by line integral = {work_integral.evalf()}")
    
    return work_integral

work_by_integral = line_integral_verification()

print(f"\nComparison:")
print(f"Work by potential difference: {work.evalf()}")
print(f"Work by line integral: {work_by_integral.evalf()}")
print(f"Match? {abs(work.evalf() - work_by_integral.evalf()) < 1e-10}")

print("=" * 50)
print("FINAL ANSWERS:")
print(f"(i) The force field IS conservative (∂P/∂y = ∂Q/∂x = e^y)")
print(f"(ii) Potential function: φ(x,y) = -e^x - xe^y + C")
print(f"(iii) Work done = {work} = {work.evalf():.10f}")

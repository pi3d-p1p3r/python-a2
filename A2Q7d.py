import sympy as sp
from sympy import symbols, exp, diff

# Define symbolic variables
x, y, t = symbols('x y t')

# Define force field F(x,y) = e^x î + xe^y ĵ
P = exp(y)        # x-component
Q = x * exp(y)    # y-component

print("Force Field: F(x,y) = e^x î + xe^y ĵ")
print(f"P(x,y) = {P}, Q(x,y) = {Q}")

# Check if the force field is conservative
Py = diff(P, y)  # = 0
Qx = diff(Q, x)  # = e^y
is_conservative = Py.equals(Qx)

print(f"\n∂P/∂y = {Py}")
print(f"∂Q/∂x = {Qx}")
print(f"Conservative? {is_conservative}")


# Find potential function φ where F = -∇φ
phi = -exp(x) - x*exp(y)

# Calculate work using potential difference
phi_initial = phi.subs({x: 1, y: 0})
phi_final = phi.subs({x: -1, y: 0})
work = phi_final - phi_initial

print(f"\nPotential function: φ(x,y) = {phi}")
print(f"Work done = {work.evalf()}")

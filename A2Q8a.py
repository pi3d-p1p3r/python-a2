import numpy as np
from scipy.integrate import dblquad
import sympy as sp

x, y = sp.symbols('x,y')

P = sp.exp(x) - y**3
Q = sp.cos(y) + x**3

Py = P.diff(y)
Qx = Q.diff(x)
integrand = sp.lambdify((y, x), Qx - Py)

W = dblquad(
    integrand,
    -1,1,
    lambda x: -np.sqrt(1-x**2),
    lambda x: np.sqrt(1-x**2)
)

print(f"Work done by the force field over the unit disk: {W[0]:.10f}")

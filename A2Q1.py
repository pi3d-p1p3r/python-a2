import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Part (a)
t = sp.symbols('t')

# (i)
r1 = sp.Matrix([sp.ln(t), sp.exp(-t), t**3])
r1_prime = r1.diff(t)
t0 = 2
r1_t0 = r1.subs(t, t0)
r1_prime_t0 = r1_prime.subs(t, t0)
print("Part (a)(i):")
print("r(t0):", r1_t0)
print("r'(t0):", r1_prime_t0)
print("Parametric equations of the tangent line:")
print("x =", r1_t0[0], "+", r1_prime_t0[0], "s")
print("y =", r1_t0[1], "+", r1_prime_t0[1], "s")
print("z =", r1_t0[2], "+", r1_prime_t0[2], "s")

# (ii)
r2 = sp.Matrix([2*sp.cos(sp.pi*t), 2*sp.sin(sp.pi*t), 3*t])
r2_prime = r2.diff(t)
t0 = sp.Rational(1, 3)
r2_t0 = r2.subs(t, t0)
r2_prime_t0 = r2_prime.subs(t, t0)
print("\nPart (a)(ii):")
print("r(t0):", r2_t0)
print("r'(t0):", r2_prime_t0)
print("Parametric equations of the tangent line:")
print("x =", r2_t0[0], "+", r2_prime_t0[0], "s")
print("y =", r2_t0[1], "+", r2_prime_t0[1], "s")
print("z =", r2_t0[2], "+", r2_prime_t0[2], "s")

# Part (b)
n1 = sp.Matrix([3, -6, -2])
n2 = sp.Matrix([2, 1, -2])
direction_vector = n1.cross(n2)
print("\nPart (b):")
print("Direction vector of the line of intersection:", direction_vector)

# Part (c)
r3 = sp.Matrix([3*t, sp.sin(t), t**2])
v = r3.diff(t)
a = v.diff(t)
print("\nPart (c):")
print("Velocity:", v)
print("Acceleration:", a)

# Plotting theta(t) vs t
t_vals = np.linspace(0, 10, 100)
theta_vals = t_vals  # Assuming theta(t) = t for simplicity
plt.plot(t_vals, theta_vals)
plt.xlabel('t')
plt.ylabel('theta(t)')
plt.title('theta(t) vs t')
plt.show()
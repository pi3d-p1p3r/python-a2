import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Part (a)
t = sp.symbols('t')
axes = sp.Matrix(['x','y','z'])

# (i)
r1 = sp.Matrix([sp.ln(t),sp.exp(-t),t**3])
tan1 = r1.diff(t)
t0 = 2
r1_sub = r1.subs(t, t0)
tan1_sub = tan1.subs(t, t0)
print("Part (a)(i):")
for i in range(len(r1)):
    print(f"{axes[i]} = {r1_sub[i]} + {tan1_sub[i]}*s")

# (ii)
r2 = sp.Matrix([2*sp.cos(sp.pi*t), 2*sp.sin(sp.pi*t), 3*t])
tan2 = r2.diff(t)
t0 = sp.Rational(1, 3)
r2_sub = r2.subs(t, t0)
tan2_sub = tan2.subs(t, t0)
print("\nPart (a)(ii):")
for i in range(len(r1)):
    print(f"{axes[i]} = {r2_sub[i]} + {tan2_sub[i]}*s")

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

# θ(t) = arccos( (v · a) / (|v| |a|) )
theta_expr = sp.acos(v.dot(a) / (v.norm() * a.norm()))
print("θ(t) =", sp.simplify(theta_expr))

# Plot θ(t) vs t
theta_func = sp.lambdify(t, theta_expr, 'numpy')
t_vals = np.linspace(0.01, 10, 500)  # avoid t=0 (zero velocity norm)
theta_vals = theta_func(t_vals)

plt.plot(t_vals, np.degrees(theta_vals))
plt.xlabel('t')
plt.ylabel('θ(t) (degrees)')
plt.title('Angle between Velocity and Acceleration vs t')
plt.grid(True, linestyle='--')
plt.show()

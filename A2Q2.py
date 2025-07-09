import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Part (a)
t = sp.symbols('t')

# Define the vector function
r = sp.Matrix([5*sp.cos(t), 4*sp.sin(t)])

# Compute the derivative
r_prime = r.diff(t)

# Evaluate at t = pi/4 and t = pi
t1 = sp.pi/4
t2 = sp.pi

r_t1 = r.subs(t, t1)
r_prime_t1 = r_prime.subs(t, t1)

r_t2 = r.subs(t, t2)
r_prime_t2 = r_prime.subs(t, t2)

print("Part (a):")
print("r(pi/4):", r_t1)
print("r'(pi/4):", r_prime_t1)
print("r(pi):", r_t2)
print("r'(pi):", r_prime_t2)

# matplotlib.pyplot.quiver expects numerical inputs, not symbolic SymPy objects.
# We convert the matrices to NumPy arrays of float64 type.
r_t1_np = np.array(r_t1, dtype=np.float64).flatten()
r_prime_t1_np = np.array(r_prime_t1, dtype=np.float64).flatten()
r_t2_np = np.array(r_t2, dtype=np.float64).flatten()
r_prime_t2_np = np.array(r_prime_t2, dtype=np.float64).flatten()

# Plotting the curve and vectors
t_vals = np.linspace(0, 2*np.pi, 100)
x_vals = 5*np.cos(t_vals)
y_vals = 4*np.sin(t_vals)

plt.figure()
plt.plot(x_vals, y_vals, label='Curve C')
plt.quiver(*r_t1_np, *r_prime_t1_np, angles='xy', scale_units='xy', scale=1, color='r', label='Tangent at pi/4')
plt.quiver(*r_t2_np, *r_prime_t2_np, angles='xy', scale_units='xy', scale=1, color='g', label='Tangent at pi')
plt.quiver(0, 0, *r_t1_np, angles='xy', scale_units='xy', scale=1, color='b', label='Position at pi/4')
plt.quiver(0, 0, *r_t2_np, angles='xy', scale_units='xy', scale=1, color='m', label='Position at pi')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curve C with Position and Tangent Vectors')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

# Part (b)
# Define the vector function for the circular helix
r_helix = sp.Matrix([sp.cos(t), sp.sin(t), t])

# Compute the derivative
r_helix_prime = r_helix.diff(t)

# Compute the arc length function
s = sp.integrate(sp.sqrt(r_helix_prime.dot(r_helix_prime)), (t, 0, t))

# Solve for t in terms of s
t_s = sp.solve(s - sp.symbols('s'), t)[0]

# Arc length parameterization
r_arc = r_helix.subs(t, t_s)

print("\nPart (b):")
print("Arc length parameterization:", r_arc)

# Compute final coordinates when s = 10
s_val = 10
t_val = t_s.subs(sp.symbols('s'), s_val)
final_coords = r_helix.subs(t, t_val)
print("Final coordinates after walking 10 units:", final_coords)

# Convert the symbolic final coordinates to a NumPy array.
final_coords_np = np.array(final_coords, dtype=np.float64).flatten()
# Convert the symbolic time value to a float for use in np.linspace.
t_val_float = float(t_val.evalf())

# Plotting the helix and final position
t_vals_helix = np.linspace(0, t_val_float, 100)
x_vals_helix = np.cos(t_vals_helix)
y_vals_helix = np.sin(t_vals_helix)
z_vals_helix = t_vals_helix

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_vals_helix, y_vals_helix, z_vals_helix, label='Helix')
ax.scatter(*final_coords_np, color='r', label='Final Position')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Circular Helix with Final Position')
ax.legend()
plt.show()
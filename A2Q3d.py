import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x, y = sp.symbols('x y', real=True)
T = 3 * x**2 * y

grad_T_expr = sp.Matrix([T.diff(x), T.diff(y)])
point = (-1, 3/2)
grad_T_at_point = grad_T_expr.subs({x: point[0], y: point[1]})

direction_vector = sp.Matrix([-1, -1/2])
unit_direction = direction_vector / direction_vector.norm()

directional_derivative_expr = grad_T_expr.dot(unit_direction)
directional_derivative_at_point = directional_derivative_expr.subs({x: point[0], y: point[1]})

print("--- Calculation Results ---")
print(f"Temperature function T(x, y) = {T}")
print(f"Gradient expression: {grad_T_expr.T}")
print(f"Direction vector: {direction_vector.T}")
print("-" * 25)
print(f"Gradient of T(x, y) at {point} is: {grad_T_at_point.T}")
print(f"Directional derivative at {point} is: {directional_derivative_at_point}")
print(f"Simplified numerical value: {directional_derivative_at_point.evalf()}")
print("\n--- Generating Plots ---")

T_func = sp.lambdify((x, y), T, 'numpy')
grad_func_x = sp.lambdify((x, y), grad_T_expr[0], 'numpy')
grad_func_y = sp.lambdify((x, y), grad_T_expr[1], 'numpy')
D_func = sp.lambdify((x, y), directional_derivative_expr, 'numpy')

x_range = np.linspace(-2, 0, 100)
y_range = np.linspace(0, 2, 100)
x_grid, y_grid = np.meshgrid(x_range, y_range)

Z_D = D_func(x_grid, y_grid)
fig1 = plt.figure(figsize=(10, 7))
ax1 = fig1.add_subplot(111, projection='3d')
surf1 = ax1.plot_surface(x_grid, y_grid, Z_D, cmap='viridis', edgecolor='none')
ax1.set_title('Surface of the Directional Derivative $D(x,y)$')
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax1.set_zlabel('Directional Derivative Value')
fig1.colorbar(surf1, shrink=0.5, aspect=5, label='Rate of Change')
plt.savefig("directional_derivative_surface.png")


# 11. Plot 2: Temperature Surface with Gradient Vector
Z_T = T_func(x_grid, y_grid)
fig2 = plt.figure(figsize=(10, 7))
ax2 = fig2.add_subplot(111, projection='3d')
surf2 = ax2.plot_surface(x_grid, y_grid, Z_T, cmap='plasma', edgecolor='none', alpha=0.8)

# Point P and the gradient vector components at P
px, py = point
pz = T_func(px, py)
grad_x_at_P, grad_y_at_P = grad_T_at_point[0], grad_T_at_point[1]

# Plot the point P on the surface
ax2.scatter([px], [py], [pz], color='red', s=100, label=f'Point P{point}', depthshade=False)
# Plot the gradient vector starting from P
ax2.quiver(px, py, pz, grad_x_at_P, grad_y_at_P, 0, color='blue', length=1, normalize=True, label='Gradient Direction at P')

ax2.set_title('Temperature Surface $T(x,y)$ with Gradient at Point P')
ax2.set_xlabel('x-axis')
ax2.set_ylabel('y-axis')
ax2.set_zlabel('Temperature T')
ax2.legend()
fig2.colorbar(surf2, shrink=0.5, aspect=5, label='Temperature')
plt.savefig("temperature_surface_with_gradient.png")

# Display the plots
plt.show()
print("Plots have been generated and saved.")

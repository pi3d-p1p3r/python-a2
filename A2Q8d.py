import numpy as np
from scipy.integrate import dblquad, quad
import matplotlib.pyplot as plt

# Surface integral calculation
def surface_integrand(r, theta):
    return (10 * r * np.cos(theta) + 4 * r * np.sin(theta) + 3) * r

surface_result, surface_error = dblquad(
    lambda r, theta: surface_integrand(r, theta), 
    0, 2 * np.pi, 
    lambda theta: 0, 
    lambda theta: 2
)

# Line integral calculation
line_integrand = lambda t: 12 * np.cos(t)**2
line_result, line_error = quad(line_integrand, 0, 2 * np.pi)

print(f"Surface integral: {surface_result:.6f}")
print(f"Line integral: {line_result:.6f}")

#Plotting the surface integral (Optional)
x = np.linspace(-2.5, 2.5, 1000); y = np.linspace(-2.5, 2.5, 1000)
X, Y = np.meshgrid(x, y)
Z = 4 - X**2 - Y**2
Z = np.where(Z >= 0, Z, np.nan) 

theta = np.linspace(0, 2 * np.pi, 1000)
circle_x = 2 * np.cos(theta); circle_y = 2 * np.sin(theta); circle_z = np.zeros_like(theta)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, alpha=0.6, rstride=20, cstride=20, color='darkcyan', edgecolor='none') 
ax.plot(circle_x, circle_y, circle_z, color='red', linewidth=3, label='Boundary Circle') 

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Paraboloid Surface and Boundary Circle for Stokes' Theorem")
ax.set_xlim([-2.5, 2.5])
ax.set_ylim([-2.5, 2.5])
ax.set_zlim([0, 5]) 
ax.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create two subplots
fig = plt.figure(figsize=(15, 6))

# First function: f(x,y) = y^2 - 2y*cos(x), 1 ≤ x ≤ 7
ax1 = fig.add_subplot(121, projection='3d')

# Create grid of points
x1 = np.linspace(1, 7, 100)
y1 = np.linspace(-5, 5, 100)  # reasonable y range
X1, Y1 = np.meshgrid(x1, y1)

# Calculate z values
Z1 = Y1**2 - 2*Y1*np.cos(X1)

# Create the surface plot
surf1 = ax1.plot_surface(X1, Y1, Z1, cmap='viridis', alpha=0.8)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.set_title('f(x,y) = y² - 2y*cos(x)')

# Add colorbar
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)

# Second function: f(x,y) = |sin(x)sin(y)|, 0 ≤ x ≤ 2π, 0 ≤ y ≤ 2π
ax2 = fig.add_subplot(122, projection='3d')

# Create grid of points
x2 = np.linspace(0, 2*np.pi, 100)
y2 = np.linspace(0, 2*np.pi, 100)
X2, Y2 = np.meshgrid(x2, y2)

# Calculate z values
Z2 = np.abs(np.sin(X2) * np.sin(Y2))

# Create the surface plot
surf2 = ax2.plot_surface(X2, Y2, Z2, cmap='viridis', alpha=0.8)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.set_title('f(x,y) = |sin(x)sin(y)|')

# Add colorbar
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
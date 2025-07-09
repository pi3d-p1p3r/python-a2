import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 2D Contour Plot for f(x,y) = 4x² + y²
x = np.linspace(-7, 7, 400)
y = np.linspace(-7, 7, 400)
X, Y = np.meshgrid(x, y)
Z = 4*X**2 + Y**2

plt.figure(figsize=(8, 7))
contours = plt.contour(X, Y, Z, levels=[1, 4, 9, 16, 26, 36], cmap='viridis')
plt.clabel(contours, inline=True, fontsize=10)
plt.title('Contour Plot of $f(x,y) = 4x^2 + y^2$')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.gca().set_aspect('equal')
plt.show()

# 3D Level Surfaces for f(x,y,z) = z² - x² - y²
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-12, 12, 200)
y = np.linspace(-12, 12, 200)
X, Y = np.meshgrid(x, y)

k_values = [1, 4, 9, 16, 26, 36]
colors = plt.cm.plasma(np.linspace(0, 1, len(k_values)))

for i, k in enumerate(k_values):
    Z_squared = k + X**2 + Y**2
    Z_pos = np.sqrt(Z_squared)
    Z_neg = -np.sqrt(Z_squared)
    
    ax.plot_surface(X, Y, Z_pos, color=colors[i], alpha=0.6, rstride=5, cstride=5)
    ax.plot_surface(X, Y, Z_neg, color=colors[i], alpha=0.6, rstride=5, cstride=5)

# Add legend
legend_proxies = [plt.Rectangle((0, 0), 1, 1, fc=colors[i], alpha=0.6) for i in range(len(k_values))]
ax.legend(legend_proxies, [f'k = {k}' for k in k_values], title='Level Surfaces')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Level Surfaces of $f(x,y,z) = z^2 - x^2 - y^2$')
ax.view_init(elev=20., azim=-65)
plt.show()
# UNIVERSITY OF DHAKA  
Department of Applied Mathematics  

### Fourth Year B.S. in Applied Mathematics  
Academic Session: 2023 – 2024  

**Course No:** AMTH 450  
**Course Title:** MATH LAB IV (Application Software)  

## Assignment – 2  
**Topic:** Solving Problems on Multivariate and Vector Calculus with Real-life Applications  

*Instruction: Write Python code to obtain the outputs and visualize the results for each problem.*

|       Name       |      Roll      | Group |
|------------------|----------------|-------|
|   Tanvir Kabir   |   SH-123-053   |   A   |

## 1. Curve Analysis  

### (a) Tangent Lines  
Find the parametric equations of the tangent line to each curve  

1.  
   $$
   \mathbf{r}(t) = \frac{3}{t}\hat{\imath} + \ln(t)\hat{\jmath} + 2\hat{k}, \quad t > 0
   $$

2.  
   $$
   \mathbf{r}(t) = e^{-t}\hat{\imath} + t\hat{\jmath} + t^3 \hat{k}
   $$

3.  
   $$
   \mathbf{r}(t) = 2\cos\left(\frac{\pi t}{2}\right)\hat{\imath} + 2\sin\left(\frac{\pi t}{2}\right)\hat{\jmath} + 3\hat{k}, \quad 0 \leq t \leq 3
   $$

### (b) Intersection of Planes  
Find a vector parallel to the line of intersection of  

$$
3x - 6y - 2z = 15, \quad 2x + 2y - 5z = 0
$$

### (c) Velocity & Acceleration  
For  
$$
\mathbf{r}(t) = 2t\hat{\imath} + 3\sin(t)\hat{\jmath} + t\hat{k}
$$  

* Compute velocity $\mathbf{v}(t)$ and acceleration $\mathbf{a}(t)$.  
* Plot $\theta(t)$ versus $t$, where $\theta(t)$ is the angle between $\mathbf{r}(t)$ and $\mathbf{v}(t)$.

## 2. Plane & Helical Curves  

### (a) Tangent Vectors on a Plane Curve  
Given  
$$
\mathbf{r}(t) = 5\cos(t)\hat{\imath} + 4\sin(t)\hat{\jmath}
$$  

* Find tangent vectors at $t = \frac{\pi}{4}$ and $t = \pi$.  
* Sketch the curve $C$ and display the position vectors $\mathbf{r}\left(\frac{\pi}{4}\right)$ and $\mathbf{r}(\pi)$ with their corresponding tangents.

### (b) Circular Helix & Arc Length  
For  
$$
\mathbf{r}(t) = (\cos(t), \sin(t), t)
$$  

1. Re-parameterize by arc length $s$ beginning at $(1,0,0)$.  
2. Determine the coordinates after the bug travels $10$ units.  
3. Provide a 3-D plot of the helix up to this point.

## 3. Frenet–Serret Frame & Multivariable Functions  

### (a) Compute $T, N, B, \kappa, \tau$  
For each curve, find the unit tangent $T$, normal $N$, binormal $B$, curvature $\kappa$ and torsion $\tau$. Plot $\kappa(t)$ and comment.

1. $$
   \mathbf{r}(t) = e^t\cos(t)\hat{\imath} + e^t\sin(t)\hat{\jmath} + 0\hat{k}
   $$

2. $$
   \mathbf{r}(t) = 2\cos(t)\hat{\imath} + 3\sin(t)\hat{\jmath} + 0\hat{k}, \quad 0 \leq t \leq 2\pi
   $$

### (b) Laplace & Cauchy-Riemann  
Verify whether  
$$
f(x,y) = y^2 - \cos(x)
$$  
satisfies Laplace's equation and the Cauchy-Riemann equations. Investigate if $f_{xy} = f_{yx}$.

### (c) Chain Rule  
Given  
$$
w = x^2 + y^2 + z^2, \quad x = \sin(\theta), \quad y = \cos(\theta), \quad z = \tan(\theta)
$$  
find $\frac{dw}{d\theta}$ at $\theta = \frac{\pi}{4}$.

### (d) Gradient & Directional Derivative  
Temperature on a plate: $T(x,y) = 3x^2y$.

1. Compute $\nabla T$ at $\left(\frac{1}{3}, 2\right)$.  
2. Find the directional derivative there in the direction $\left(-\frac{1}{2}, -1\right)$.  
3. Plot the directional derivative for $-2 \leq x \leq 2, 0 \leq y \leq 2$ and visualize it on the surface.

## 4. Contour Plots & 3-D Surfaces  

### (a) Level Curves  
Sketch contour plots for  

1. $f(x,y) = x^2 + y^2$  
2. $f(x,y,z) = z^2 - x^2 - y^2$  

using level values $k = 1, 4, 9, 16, 26, 36$.

### (b) 3-D Visualization  
Plot  

* $f(x,y) = 2y - \frac{y^2}{7}, \quad -\pi \leq x \leq \pi, \quad 0 \leq y \leq 2$  
* $f(x,y) = \sin(x)\sin(y), \quad 0 \leq x \leq 2\pi, \quad 0 \leq y \leq 2\pi$

### (c) Relative Extrema & Saddle Points  
Locate all relative extrema and saddle points of  

1. $f(x,y) = x^4 - 4xy^4$  
2. $f(x,y) = x^2e^{-y^2} - 4e^{-y^2}$  

Confirm results via graphs.

## 5. Tangent Planes, Normals & Lagrange Multipliers  

### (a) Ellipsoid  
$$
\frac{x^2}{4} + \frac{y^2}{18} + z^2 = 1
$$  
at $(1, 2, 1)$  

1. Equation of the tangent plane.  
2. Parametric equations of the normal line.  
3. Acute angle between the tangent plane and the $xy$-plane.  
4. Provide a visualization.

### (b) Hottest Point via Lagrange Multipliers  
For the surface  
$$
\frac{x^2}{4} + \frac{y^2}{4} + \frac{z^2}{16} = 1
$$  
with temperature  
$$
T(x,y,z) = 600 + \frac{8x}{4} + \frac{yz}{16} - z^2
$$  
find the hottest point on the probe.

## 6. Multiple & Surface Integrals  

### (a) Triple and Double Integrals  

1. $$
   \int_0^1 \int_0^1 \int_{-2}^2 x e^{y^2} \cos(z^2) \, dz \, dy \, dx
   $$

2. $$
   \iint_R xy \, dA, \quad R: 0 \leq x \leq 1, 0 \leq y \leq 1, x + y \leq 1
   $$

### (b) Surface Area  
Find the area of the portion of $z = 4 - x^2$ above  
$R: 0 \leq x \leq 1, 0 \leq y \leq 4$.

### (c) Volume Inside a Paraboloid & Cylinder  
Volume beneath $z = 4 - x^2 - y^2$, above $z = 0$, and inside $(x-1)^2 + y^2 = 1$.

## 7. Average Temperature, Line Integrals & Mass  

### (a) Average Temperature  
For $T(x,y) = 10 - 8x^2 - 2y^2$ over $0 \leq x \leq 1, 0 \leq y \leq 2$.

### (b) Helical Line Integral  
Evaluate  
$$
\int_C (xy + z^3) \, ds
$$  
from $(1,0,0)$ to $(1,0,\pi)$ along  
$x = \cos(t), y = \sin(t), z = t, 0 \leq t \leq \pi$.

### (c) Mass of a Cylinder  
Radius $r$, height $h$, density $\rho(x,y) = x^2 + y^2$.

### (d) Conservative Field  
Given $\mathbf{F}(x,y) = e^y\hat{\imath} + xe^y\hat{\jmath}$:

1. Verify conservativeness.  
2. Find potential $\phi$.  
3. Compute work from $(1,0)$ to $(-1,0)$ along the semicircle $C$.

## 8. Green, Divergence & Stokes Theorems  

### (a) Work via Green's Theorem  
$$
\mathbf{F}(x,y) = e^{\cos(x^3)}\hat{\imath} + (y^3 + x^3)\hat{\jmath}, \quad C: x^2 + y^2 = 1 \text{ (counter-clockwise)}
$$

### (b) Surface Integral over a Sphere  
Evaluate  
$$
\iint_\sigma 2x \, dS
$$  
on $x^2 + y^2 + z^2 = 1$.

### (c) Flux via Divergence Theorem  
$$
\mathbf{F}(x,y,z) = x^3\hat{\imath} + y^3\hat{\jmath} + 2z\hat{k}, \quad \sigma: x^2 + y^2 = 9, 0 \leq z \leq 2
$$

### (d) Verify Stokes' Theorem  
For $\mathbf{F}(x,y,z) = 2z\hat{\imath} + 3x\hat{\jmath} + 5y\hat{k}$,  
surface $\sigma: z = 4 - x^2 - y^2, z \geq 0$ (upward normal),  
boundary $C: x^2 + y^2 = 4$ in the $xy$-plane.

*End of Assignment – 2*

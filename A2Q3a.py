import numpy as np
import matplotlib.pyplot as plt

e_t = np.exp(t)
def derivatives_curve1(t):
    r_p  = np.array([ e_t, e_t*(np.cos(t)-np.sin(t)), e_t*(np.sin(t)+np.cos(t)) ])
    r_pp = np.array([ e_t, e_t*(-2*np.sin(t)), e_t*( 2*np.cos(t)) ])
    return r_p, r_pp

def derivatives_curve2(t):
    r_p  = np.array([-2*np.sin(t),  3*np.cos(t), 0])
    r_pp = np.array([-2*np.cos(t), -3*np.sin(t), 0])
    return r_p, r_pp

def compute_TNB(r_p, r_pp):
    T = r_p / np.linalg.norm(r_p)
    B = np.cross(r_p, r_pp)
    B /= np.linalg.norm(B)
    N = np.cross(B, T)
    return T, N, B

def curvature(r_p, r_pp):
    cross = np.cross(r_p, r_pp)
    return np.linalg.norm(cross) / (np.linalg.norm(r_p)**3)

def torsion(r_p, r_pp, r_ppp):
    cross = np.cross(r_p, r_pp)
    norm_cross = np.linalg.norm(cross)
    if norm_cross == 0:
        return 0.0
    return np.dot(cross, r_ppp) / (norm_cross**2)

def derivatives_curve1_third(t):
    return np.array([ e_t, e_t*(-2*np.cos(t)-2*np.sin(t)), e_t*(-2*np.sin(t)+2*np.cos(t)) ])

def derivatives_curve2_third(t):
    return np.array([ 2*np.sin(t), -3*np.cos(t), 0 ])

# Evaluate at t = 0
t0 = 0
r1_p, r1_pp    = derivatives_curve1(t0)
r1_ppp         = derivatives_curve1_third(t0)
T1, N1, B1     = compute_TNB(r1_p, r1_pp)
kappa1        = curvature(r1_p, r1_pp)
tau1          = torsion(r1_p, r1_pp, r1_ppp)

r2_p, r2_pp    = derivatives_curve2(t0)
r2_ppp         = derivatives_curve2_third(t0)
T2, N2, B2     = compute_TNB(r2_p, r2_pp)
kappa2        = curvature(r2_p, r2_pp)
tau2          = torsion(r2_p, r2_pp, r2_ppp)

print("Curve 1 at t=0:")
print(f"  T = {T1}")
print(f"  N = {N1}")
print(f"  B = {B1}")
print(f"  κ = {kappa1:.6f}")
print(f"  τ = {tau1:.6f}\n")

print("Curve 2 at t=0:")
print(f"  T = {T2}")
print(f"  N = {N2}")
print(f"  B = {B2}")
print(f"  κ = {kappa2:.6f}")
print(f"  τ = {tau2:.6f}\n")

t = np.linspace(0, 2*np.pi, 1000)
kappa1_vals = [curvature(*derivatives_curve1(ti)) for ti in t]
kappa2_vals = [curvature(*derivatives_curve2(ti)) for ti in t]

# Plot curvature for Curve 1
plt.figure(figsize=(10, 6))
plt.plot(t, kappa1_vals, color='C0', linewidth=2, label='Curve 1')
plt.title('Curvature (κ) vs t for Curve 1')
plt.xlabel('t')
plt.ylabel('κ')
plt.grid(True)
plt.legend()
plt.show()

# Plot curvature for Curve 2
plt.figure(figsize=(10, 6))
plt.plot(t, kappa2_vals, color='C1', linewidth=2, label='Curve 2')
plt.title('Curvature (κ) vs t for Curve 2')
plt.xlabel('t')
plt.ylabel('κ')
plt.grid(True)
plt.legend()
plt.show()

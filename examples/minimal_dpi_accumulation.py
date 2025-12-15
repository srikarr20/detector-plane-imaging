"""
Minimal Detector-Plane Imaging (DPI) example.

Demonstrates detector-plane accumulation of a coherent field
without particles, optics, or post-selection.
"""
import numpy as np
import matplotlib.pyplot as plt

# --- Grid ---
N = 256
L = 10.0
x = np.linspace(-L, L, N)
X, Y = np.meshgrid(x, x)

# --- Field definition (simple coherent packet) ---
def field(x, y, t):
    r2 = x**2 + y**2
    return np.exp(-r2) * np.cos(5 * r2 - t)

# --- Detector-plane sampling ---
n_frames = 100
accumulated = np.zeros((N, N))

for t in np.linspace(0, 10, n_frames):
    phi = field(X, Y, t)
    intensity = phi**2          # detector-plane intensity
    accumulated += intensity    # long-exposure accumulation

accumulated /= n_frames

# --- Plot ---
plt.figure(figsize=(6, 6))
plt.imshow(accumulated, extent=[-L, L, -L, L], cmap="inferno")
plt.colorbar(label="Accumulated intensity")
plt.title("Minimal DPI: Detector-Plane Accumulation")
plt.xlabel("x")
plt.ylabel("y")
plt.tight_layout()
plt.show()

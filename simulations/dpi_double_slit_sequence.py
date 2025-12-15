"""
Complete Detector-Plane Imaging (DPI) sequence.

Field → detector-plane accumulation → double-slit probing →
visibility loss via decoherence.

Classical, reproducible, measurement-plane focused.
"""

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Grid
# ----------------------------
N = 256
L = 10.0
x = np.linspace(-L, L, N)
X, Y = np.meshgrid(x, x)

# ----------------------------
# Field definition
# ----------------------------
def field(x, y, t):
    r = np.sqrt(x**2 + y**2)
    return np.exp(-r**2) * np.cos(8 * r - t)

# ----------------------------
# Detector-plane accumulation
# ----------------------------
n_frames = 120
accumulated = np.zeros((N, N))

for t in np.linspace(0, 12, n_frames):
    phi = field(X, Y, t)
    accumulated += phi**2

accumulated /= n_frames

# ----------------------------
# Double-slit mask
# ----------------------------
slit_sep = 1.5
slit_width = 0.3

mask = (
    ((np.abs(X - slit_sep / 2) < slit_width) |
     (np.abs(X + slit_sep / 2) < slit_width))
)

illumination = accumulated * mask

# ----------------------------
# Far-field propagation
# ----------------------------
def far_field(intensity):
    F = np.fft.fftshift(np.fft.fft2(intensity))
    return np.abs(F)**2

far_coherent = far_field(illumination)

# ----------------------------
# Decoherence (phase scrambling)
# ----------------------------
noise = 0.4 * np.random.randn(*illumination.shape)
far_decoherent = far_field(illumination + noise)

# ----------------------------
# Plot
# ----------------------------
fig, axs = plt.subplots(2, 3, figsize=(12, 8))

axs[0,0].imshow(accumulated, cmap="inferno")
axs[0,0].set_title("Detector-Plane Accumulation")

axs[0,1].imshow(mask, cmap="gray")
axs[0,1].set_title("Double-Slit Mask")

axs[0,2].imshow(illumination, cmap="inferno")
axs[0,2].set_title("Illumination at Slits")

axs[1,0].imshow(np.log(far_coherent + 1e-6), cmap="turbo")
axs[1,0].set_title("Far Field (Coherent)")

axs[1,1].imshow(np.log(far_decoherent + 1e-6), cmap="turbo")
axs[1,1].set_title("Far Field (Decoherent)")

axs[1,2].plot(
    far_coherent[N//2] / far_coherent.max(),
    label="Coherent"
)
axs[1,2].plot(
    far_decoherent[N//2] / far_decoherent.max(),
    label="Decoherent"
)
axs[1,2].set_title("Visibility Cross-Section")
axs[1,2].legend()

for ax in axs.flat:
    ax.axis("off")

plt.tight_layout()
plt.savefig("figures/dpi_sequence.png", dpi=300, bbox_inches="tight")
plt.show()


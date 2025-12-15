# DPI Simulations

This directory contains **minimal, reproducible simulations** demonstrating the
core concepts of **Detector-Plane Imaging (DPI)** and **Imprint Field Dynamics (IFD)**.

All simulations in this directory are:
- Fully classical (field-level)
- Reproducible using standard Python tools
- Focused on measurement-plane structure rather than particle-based interpretations

The purpose of these simulations is to show how **structured interference and
visibility changes arise from pre-existing field coherence** sampled at a detector plane.

---

## Core Simulation

### `dpi_double_slit_sequence.py`

This script implements a complete, minimal DPI + IFD sequence:

1. **Imprint Field Dynamics (IFD)**  
   A localized, oscillatory field excitation (oscillon-like) generates a stable,
   time-averaged intensity imprint at the detector plane.

2. **Detector-Plane Imaging (DPI)**  
   The detector plane is treated as an active measurement geometry. Accumulation
   over time reveals pre-existing spatial coherence in the field.

3. **Double-Slit Probing**  
   A double-slit mask samples the detector-plane imprint, producing structured
   illumination at the apertures.

4. **Far-Field Interference**  
   Far-field propagation of the structured illumination yields high-visibility
   interference fringes.

5. **Decoherence Model**  
   Simple phase scrambling models loss of coherence (correlation-length decay),
   reducing fringe visibility without altering slit geometry.

The resulting visualization is saved to:


# 🧲 Electromagnetism: Magnetic Force on a Wire

This module provides a computational tool to determine the **Magnetic Force** ($F$) acting on a current-carrying wire placed in a magnetic field. It serves as a practical application of the Lorentz force principle using Python's functional programming.

## 🧪 Scientific Overview

![Magnetic Force on Wire Diagram]()

When an electric current flows through a wire placed within an external magnetic field, the moving charges experience a force. For a straight wire of length $L$ carrying a current $I$ in a uniform magnetic field $B$, the magnitude of the force (assuming the wire is perpendicular to the field) is given by:

$$F = B \times I \times L$$

Where:
* **Magnetic Force ($F$):** Measured in Newtons ($N$).
* **Magnetic Field ($B$):** The magnetic flux density, measured in Tesla ($T$).
* **Current ($I$):** The electric current flowing through the wire, measured in Amperes ($A$).
* **Length ($L$):** The length of the wire segment within the field, measured in Meters ($m$).

## 💻 Logic & Implementation
This script follows the high standards of the Physics Python Tools Gallery:
* **Function-Based Design:** Encapsulates the calculation within the `Magnetic_Force` function for modularity.
* **Input Validation:** Uses `try-except` blocks to handle non-numeric inputs and ensure the script doesn't crash.
* **Physical Constraints:** Includes nested `if-elif` logic to ensure $B$, $I$, and $L$ are non-zero, as a zero value in any parameter results in no magnetic force.
* **Clear Output:** Provides the result formatted in Newtons for easy interpretation.

## 🚀 Usage
Run the script and enter the following parameters when prompted:
1. **Magnetic Field ($B$):** The strength of the external field.
2. **Current ($A$):** The amount of current passing through the wire.
3. **Length ($m$):** The length of the wire exposed to the magnetic field.

---

### 📂 Source Code
You can view and download the full Python script here:  
**[👉 magnetic_force_on_wire.py](./magnetic_force_on_wire.py)**

---
*Developed by vedika_apte | M.Sc. Physics | Python Developer*

*Part of the Physics Python Tools Gallery*

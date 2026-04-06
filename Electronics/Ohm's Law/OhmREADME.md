# ⚡ Electronics: Ohm's Law Calculator

This module provides a robust computational tool to determine the relationship between **Voltage** ($V$), **Current** ($I$), and **Resistance** ($R$). It serves as a practical application of circuit theory using Python's functional programming.

## 🧪 Scientific Overview
![Ohm's Law Relationship Diagram](./ohms_law_diagram.png)

Ohm's Law is a fundamental principle in electronics, stating that the current through a conductor between two points is directly proportional to the voltage across the two points.

$$V = I \times R$$

Where:
* **Voltage ($V$):** Potential difference measured in Volts ($V$).
* **Current ($I$):** Flow of electric charge measured in Amperes ($A$).
* **Resistance ($R$):** Opposition to current flow measured in Ohms ($\Omega$).

## 💻 Logic & Implementation
This script demonstrates high-level programming practices:
* **Dynamic Solving:** Independent functions to solve for the unknown variable based on user input.
* **Input Validation:** Converts user input to floats and handles non-numeric errors using `try-except` blocks.
* **Safety Constraints:** Checks for zero-division errors (e.g., Resistance = 0) before performing calculations.

## 🚀 Usage
Run the script and select which parameter you wish to calculate:
1. **Calculate Voltage:** Provide Current and Resistance.
2. **Calculate Current:** Provide Voltage and Resistance.
3. **Calculate Resistance:** Provide Voltage and Current.

---
### 📂 Source Code
You can view and download the full Python script here: 
**[👉 ohms_law.py](./ohms_law.py)**
---
*Part of the Physics Python Tools Gallery*

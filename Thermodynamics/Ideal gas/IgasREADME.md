# 🌡️ Thermodynamics: Ideal Gas Law Calculator

This module provides a computational tool to determine the **Number of Moles** ($n$) of a gas using the **Ideal Gas Equation**. It serves as a fundamental application of kinetic molecular theory using Python's functional programming.

## 🧪 Scientific Overview

![Ideal Gas Law Diagram]()

The Ideal Gas Law is the equation of state of a hypothetical ideal gas. It is a good approximation of the behavior of many gases under many conditions, although it has several limitations.

The state of an amount of gas is determined by its pressure, volume, and temperature according to the equation:

$$PV = nRT$$

To find the number of moles ($n$), we rearrange the formula:

$$n = \frac{PV}{RT}$$

Where:
* **Pressure ($P$):** Measured in Pascals ($Pa$).
* **Volume ($V$):** Measured in cubic meters ($m^3$).
* **Temperature ($T$):** Measured in Kelvin ($K$).
* **Ideal Gas Constant ($R$):** Approximately $8.314 \, J/(mol \cdot K)$.
* **Amount of Substance ($n$):** Measured in moles ($mol$).

## 💻 Logic & Implementation
This script follows the established standards of the Physics Python Tools Gallery:
* **Constant Integration:** Hardcodes the universal gas constant ($R = 8.314$) for ease of use.
* **Function-Based Design:** Encapsulates the algebraic rearrangement in the `Ideal_gas_equation` function.
* **Error Handling:** Employs `try-except` blocks to catch non-numeric inputs.
* **Safety Constraints:** Includes a logical check to ensure Temperature is not zero, preventing division errors ($1/0$).

## 🚀 Usage
Run the script and enter the following parameters when prompted:
1. **Pressure ($Pa$):** The pressure exerted by the gas.
2. **Volume ($m^3$):** The space occupied by the gas.
3. **Temperature ($K$):** The absolute temperature of the system.

The program will output the total number of moles ($mol$) present in the system.

---

### 📂 Source Code
You can view and download the full Python script here:  
**[👉 ideal_gas_law.py](./ideal_gas_law.py)**

---
*Developed by vedika_apte | M.Sc. Physics | Python Developer*

*Part of the Physics Python Tools Gallery*

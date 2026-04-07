# 🍎 Mechanics: Newton's Second Law Calculator

This module provides a streamlined computational tool to determine the **Net Force** ($F$) acting on a body. It serves as a practical implementation of classical mechanics using Python's functional programming.

## 🧪 Scientific Overview
Newton's Second Law of Motion defines the relationship between an object's mass and the amount of force needed to accelerate it. It states that the acceleration of an object is directly proportional to the net force acting upon it and inversely proportional to its mass.

The fundamental formula is:

$$F = m \times a$$

Where:
* **Force ($F$):** The vector sum of all forces, measured in Newtons ($N$).
* **Mass ($m$):** The quantity of matter in the object, measured in kilograms ($kg$).
* **Acceleration ($a$):** The rate of change of velocity, measured in $m/s^2$.

## 💻 Logic & Implementation
This script demonstrates clean and reliable programming practices:
* **Function-Based Design:** Utilizes a dedicated `Force` function for modularity and reusability.
* **Input Validation:** Employs `try-except` blocks to handle non-numeric inputs and maintain program stability.
* **Safety Constraints:** Includes a logical check to ensure mass is not zero, preventing physically impossible calculations.
* **Standard Constants:** Defaults to Earth's gravitational acceleration ($9.8 \text{ m/s}^2$) for rapid real-world computations.

## 🚀 Usage
Run the script and enter the following parameter when prompted:
1. **Mass ($kg$):** The mass of the object you are analyzing.

The program will output the total Force in Newtons, assuming a standard acceleration of $9.8 \text{ m/s}^2$.

---

### 📂 Source Code
You can view and download the full Python script here:  
**[👉 newtons_2nd_law_of_motion.py](./newtons_2nd_law_of_motion.py)**

---
*Developed by vedika_apte | M.Sc. Physics | Python Developer*

*Part of the Physics Python Tools Gallery*

# -*- coding: utf-8 -*-
"""
python program to find magnetic moment using defined function 

@author: vedika_apte
"""

# Calculate magnetic moment using defined function

def Magnetic_moment(I,A):
    return (I*A)

try:
    current = input("Enter current(A):")
    area = input("Enter area in meter square(m^2):")
    
    I = float(current)
    A = float(area)
    
    if I==0:
        print("Error: current cannot be zero")
    elif A==0:
        print("Error: area cannot be zero")
    else:
        m = Magnetic_moment(I,A)
        print("Magnetic moment is:" , m , "Am^2")
except:
    print("Error: Enter a numeric value")

Magnetic_moment(I,A)

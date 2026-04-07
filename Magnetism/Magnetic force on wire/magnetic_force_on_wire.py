# -*- coding: utf-8 -*-
"""
Python program for magnetic force acting on wire using defined function

@author: vedika_apte
"""

# Calculate magnetic force acting on wire 
 
def Magnetic_Force(B,I,L):
    return B*I*L

try:
    field = input("Enter Magnetic field(B):")
    current = input("Enter current(A):")
    length = input("Enter length of wire in meter(m):")
    
    B = float(field)
    I = float(current)
    L = float(length)
    
    if B==0:
        print("Error: magnetic field cannot be zero")
    elif I==0:
        print("Error: current cannot be zero")
    elif L==0:
        print("Error: length cannot be zero")
    else:
        F = Magnetic_Force(B,I,L)
        print("Mangnetic force on wire is:" , F , "N")
except:
    print("Error: Enter a numeric value")
    
Magnetic_Force(B,I,L)

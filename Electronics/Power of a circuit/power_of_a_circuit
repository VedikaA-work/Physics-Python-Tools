# -*- coding: utf-8 -*-
"""
Python program to calculate power of circuit using defined function
[Also includes calculation of resistance by Ohm's law']

@author: vedika_apte
"""

# Calculate power of circuit using defined function

# Calculate power using voltage and current 

def Power_VI(V,I):
    return (V*I)

# Calculate resistance by ohm's law using defined function
def Ohms_Law(V,I):
    return (V/I)

# Calculate power using current and resistance
def Power_IR(I,R):
    return (I*I*R)

try:
    voltage = input("Enter voltage(V):")
    current = input("Enter current(A):")

    V = float(voltage)
    I = float(current)
    
    if V==0 or I==0:
        print("Error: Enter a positive value")
    else:
        P = Power_VI(V,I)
        print("Power = (V*I) = " , P ,"Watt" )
        
    if I==0:
        print("Error: Current cannot be zero")
    else:
        R = Ohms_Law(V,I) 
        print("Resistance = (V/I) = " , R , "\u03A9") 
        
    current = input("Enter current(A):")
    resistance = input("Enter resistance(ohm):")
    
    I = float(current)
    R = float(resistance)
    
    if I==0 or R==0:
        print("Error: Enter positive value")
    else:
        power = Power_IR(I,R)
        print("Power = (I^2*R) = " , power , "Watt")
    
except:
    print("Error: Enter a numeric value")
    
Power_VI(I,V) 

Ohms_Law(V,I)

Power_IR(I,R)

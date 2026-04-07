# -*- coding: utf-8 -*-
"""
python program to find refractive index using defind function

@author: vedika_apte
"""

# Calculate refractive index 

def Refractive_Index(c,v):
    return (c/v)

try:
    vel = input("Enter velocity(m/s):")
    v = float(vel)
    
    c = 3.0
    
    if v==0:
        print("Velocity cannot be zero")
    else:
        n = Refractive_Index(c,v)
        print("Refractive Index =" , n)

except:
    print("Error: Enter a numeric value")
    
Refractive_Index(c,v)

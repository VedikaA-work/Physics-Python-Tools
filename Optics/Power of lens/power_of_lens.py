# -*- coding: utf-8 -*-
"""
python program for calculating lens power using focal length

@author: vedika_apte
"""
# Calculate lens power using focal length
 
def Lens_Power(f_cm):
    return (1.0/f_cm)

try:
    focal_m = input("Enter focal length in meter(m):")
    f_m = float(focal_m)
    
    f_cm = f_m / 100.0
    
    if f_cm==0:
        print("Error: focal length cannot be zero")
    else:
        P = Lens_Power(f_cm)
        print("Power of lens =" , P , "/cm")
except:
    print("Error: Enter a numeric value")
    
Lens_Power(f_cm)

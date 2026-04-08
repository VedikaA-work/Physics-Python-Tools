# -*- coding: utf-8 -*-
"""
Python program to find speed of sound wave using defined function

@author: vedika_apte
"""

# Calculate Speed of sound wave 

# Calculate frequency 

def Freq(T):
    return 1/T

try:
    time = input("Enter time period is second(s):")
    T = float(time)
    
    if T==0:
        print("Error: time cannot be zero")
    else:
        f = Freq(T)
        print("Frequency is:" , f , "Hz")
except:
    print("Error: Enter a numeric value")
    
Freq(T)

# Calculate speed of sound wave
def Wave_Speed(Lambda,f):
    return Lambda*f

try:
    wavelength = input("Enter wavelength[m]:")
    freq = input("Enter frequency[Hz]:")
    
    Lambda = float(wavelength)
    f = float(freq)
    
    if Lambda==0:
        print("Error: wavelength cannot be zero")
    elif f==0:
        print("Error: frequency cannot be zero")
    else:
        v = Wave_Speed(Lambda,f)
        print("Speed of sound wave is =" , v , "m/s")

except:
    print("Error: Enter a numeric value")

Wave_Speed(Lambda,f)

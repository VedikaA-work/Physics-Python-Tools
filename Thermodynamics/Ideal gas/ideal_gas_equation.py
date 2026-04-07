# -*- coding: utf-8 -*-
"""
python program to find "n" moles of gas using ideal gas equation

@author: vedika_apte
"""
# Calculate "n" no. of moles using ideal gas equation

def Ideal_gas_equation(P,V,n,R,T):
    return (P*V)/(R*T)

try:
    pressure = input("Enter pressure[Pa]:")
    volume = input("Enter volume[m^3]:")
    temp = input("Enter temperature[K]:")
    gas_constant = 8.314
    
    P = float(pressure)
    V = float(volume)
    T = float(temp)
    R = float(gas_constant)
    
    if T==0:
        print("Temprature cannot be zero")
    else:
        no_mol = Ideal_gas_equation(P,V,n,R,T)
        print("Number of moles =" , no_mol , "mol")
except:
    print("Error: Enter a numeric value")

Ideal_gas_equation(P,V,n,R,T)

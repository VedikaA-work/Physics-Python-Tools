# -*- coding: utf-8 -*-
"""
Python program to find speed of sound in medium(soli,liquid,gas)
Uses elastic modulus to calculate speed of sound

@author: vedika_apte
"""

# Calculate speed of sound in media (solid , liquid , gas) 

print("Find speed of sound in different media like solid,liquid,gas")
print("1:For solid medium select 1 [uses Young's modulus]")
print("2:For liquid medium select 2 [uses Bulk modulus]")
print("3:For gas medium select 3 [uses adiabatic index {Cp/Cv} and Pressure]")

medium = input("Select medium (1/2/3):") 
medium = int(medium)

if medium<1 or medium>3:
    print("Error: Please select from (1/2/3):")
else:
    density = input("Enter density[kg/m^3]:")
    d = float(density)
    
# Calculate speed in solid
def Sound_Speed_Solid(Y,d):
    return (Y/d)**0.5

# Calculate speed in liquid
def Sound_Speed_Liquid(B,d):
    return (B/d)**0.5

# Calculate speed in gas
def Sound_Speed_Gas(gamma,P,d):
    return (gamma*P/d)**0.5

try:
    if medium==1:
        young = input("Enter young's modulus:")
        Y = float(young)
    
        v_solid = Sound_Speed_Solid(Y,d)
        print("Speed of sound in solid medium is:" , v_solid , "m/s")
    
    elif medium==2:
        bulk = input("Enter bulk modulus:")
        B = float(bulk)
    
        v_liquid = Sound_Speed_Liquid(B,d)
        print("Speed of sound in liquid medium is:" , v_liquid , "m/s")
        
    elif medium==3:
        adiabatic_index = input("Enter adiabatic index(Cp/Cv):")
        pressure = input("Enter pressure:")
    
        gamma = float(adiabatic_index)
        P = float(pressure)
    
        v_gas = Sound_Speed_Gas(gamma,P,d)
        print("Speed of sound in ga medium is:" , v_gas , "m/s")
        print("Speed of sound in gas medium is temperature dependent")
        
except:
    print("Error: Enter a numeric value")

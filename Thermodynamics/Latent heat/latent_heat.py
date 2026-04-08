# -*- coding: utf-8 -*-
"""
Python program to find Latent heat (or fusion , of vaporization)

@author: vedika_apte
"""

# Calculate Latent heat (of fusion,of vaporization)

# Calulate Latent heat for solid or liquid  
    
print("Find latent heat for solid,liquid")
print("1:For latent heat of fusion select 1 [solid-to-liquid]")
print("2:For latent heat of vaporiztion select 2 [liquid-to-gas]")

select = input("Select option 1 or 2:")
select = int(select)

if select<1 or select>2:
    print("Error: Please select 1 or 2:")
else:
    mass = input("Enter mass in Kg[Kg]:")
    m = float(mass)

# Calculate Latent heat of fusion
def L_heat_fusion(m,Lf):
    return m*Lf

# Calculate Latent heat of vaporiztion
def L_heat_vaporization(m,Lv):
    return m*Lv

try:
    if select==1:
        heat1 = input("Enter Latent heat of fusion:")
        Lf = float(heat1)
    
        Q1 = L_heat_fusion(m,Lf)
        print("Total Heat Energy is:" , Q1 , "J/Kg")
    
    elif select==2:
        heat2 = input("Enter Latent heat of vaporiztion:")
        Lv = float(heat2)
    
        Q2 = L_heat_vaporization(m,Lv)
         print("Total Heat Energy is:" , Q2 , "J/Kg")

except:
    print("Error: Enter a numeric value")

# -*- coding: utf-8 -*-
"""
Python program to find young's modulus using defined function 
   also includes calculations for stress and strain

@author: vedika_apte
"""

# Calculate Young's Modulus using defined function
# Calculate Stress = force / area

def Stress(f,a):
    return f/a

try:
    Force = input("Enter force:")
    Area = input("Enter area in meter square:")

    f = float(Force)
    a = float(Area)
       
    if a==0:
        print("Error: Area cannot be zero")
    else:
        stress_value = Stress(f,a)
        print("Stress is:", stress_value , "N/m^2")
except:
    print("Error: Enter a numeric value") 

Stress(f,a)

# Calculate strain = change in length / original length
def Strain(n,L):
    return n/L

try:
    new_length = input("Enter new length:(m)")
    original_length = input("Enter original length(m):")
    
    m = float(new_length)
    L = float(original_length)
    
    n = m-L
       
    if L==0:
        print("Error: original length cannot be zero")
    else:
        strain_value = Strain(n,L)
        print("Strain is:", strain_value)
except:
    print("Error: Enter a numeric value") 

Strain(n,L)

# Calculate Young's Modulus using defined fuction 
def Young_Modulus(s , st):
    return s/st

try:
    s = stress_value 
    st = strain_value 
    if st==0:
        print("Error: Denominator cannot be zero")
    else:
        young_modulus = Young_Modulus(s , st)
        print("Young's Modulus is:" , young_modulus , "N/m^2")
except:
    print("Error: Enter a numeric value") 
  

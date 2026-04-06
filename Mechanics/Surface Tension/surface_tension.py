# -*- coding: utf-8 -*-
"""
Python code to find surface tension and surface energy 
   [Also include surface tension for soap bubble and spherical droplet]

@author: vedika_apte
"""

# Calculate Surface Tension 
def SurfaceTension(f,l):
    return (f/l)

# Calculate Surface Tension for Soap Bubble (Two surfaces) 
def Surface_Tension_of_Soap_Bubble(f,L):
    return (f/L)

# Calculate Surface Tension of Spherical Droplet (one surface)
def Surface_Tension_of_Spherical_Droplet(T,r):
    return (2*T/r)

# Calculate Surface Energy 
def Surface_Energy(W,delta_A):
    return (W/delta_A)

try:
    Force = input("Enter force(m):")
    length = input("Enter length in meter square(m):")
    radius = input("Enter radius in meter square(m):")
    work = input("Enter work/energy(J):")
    delta_a = input("Enter change in area in meter square(m):")
    f = float(Force)
    l = float(length)
    L = 2*l
    r = float(radius)
    W = float(work)
    delta_A = float(delta_a)
    
    if l==0:
        print("Error: length cannot be zero")
    else:
        T = SurfaceTension(f,l)
        print("Surface Tension is:" , T , "N/m")
    
    if l==0:
        print("Error: length cannot be zero")
    else:
        gamma = Surface_Tension_of_Soap_Bubble(f,L)
        print("Surface Tension of Soap Bubble is:" , gamma , "N/m")
        
    if r==0:
        print("Error: radius cannot be zero")
    else:
        P = Surface_Tension_of_Spherical_Droplet(T,r)
        print("Surface Tension of Spherical Droplet is:" , P , "N/m^2")
    
    if delta_a==0:
        print("Error: change in area cannot be zero")
    else:
        surface_energy = Surface_Energy(W,delta_A)
        print("Surface Energy is:" , surface_energy , "J/m^2 or N/m")
    
except:
    print("Error: Enter a numeric value")

SurfaceTension(f,l)

Surface_Energy(W,delta_A)

Surface_Tension_of_Soap_Bubble(f,L)

Surface_Tension_of_Spherical_Droplet(T,r)

# coding: utf-8
#'''
# @author : vedika_apte
#'''
# Program to find Resistance by Ohm's Law 

voltage = input("Enter voltage(in mV):") 
current = input("Enter current(in mA):") 

try:
    V = float(voltage)
    I = float(current)

    if I==0:
        print("Can't divide by zero : change current value")
    else:
        print("Voltage and Current values are in range")
#Calculating Resistance by Ohm's Law 
    R = V/I
    print("Resistance is:", R, "m\u03A9")

except:
    print("Error: Enter an integer value")
  

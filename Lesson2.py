# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 10:14:49 2023

@author: lena
"""

import math as m

temp_celsius = float(input("Enter the temperature in Celsius"))
temp_kelvin = temp_celsius + 273.15
print("For {}°C you get {} K" . format(temp_celsius, temp_kelvin))

l = float(input("Enter the edge value"))
area = 6 * l ** 2
volume = l ** 3
print("For an edge value of {}, the area is {} and the volume is {}" . format(l, area, volume))

nb10 = int(input("How many 10 euro banknotes do you have ?"))
nb20 = int(input("How many 20 euro banknotes do you have ?"))
nb50 = int(input("How many 50 euro banknotes do you have ?"))
total = nb10 * 10 + nb20 * 20 + nb50 * 50
print("You have a total of {} euros" . format(total))

r = float(input("Enter the radius of the circle in cm"))
L = 2 * m.pi * r
A = m. pi * r**2
print("For a radius of {} cm the length of the circumference is {} cm and the value of the area is {} cm²" . format(r, L, A))

r = float(input("Enter the radius of the sphere in cm"))
area = 4 * r**2 *m.pi
volume = 4/3 * m. pi * r**3
print("The sphere of radius {} cm has an area of {} cm² and a volume of {} cm^3" . format(r, area, volume))

A = float(input("Enter the value of A in s^-1"))
Ea = float(input("Enter the value of Ea in kJ/mol"))
T = float(input("Enter the value of T in °C"))
T = T + 273.15
R = 8.3144621
k = A * m.exp((-Ea)/(R*T))
print("The rate constant of the reaction is {}" . format(k))


a = float(input("Enter the value of the first side"))
b = float(input("Enter the value of the second side"))
angle = float(input("Enter the value of the angle in °"))
c = m.sqrt(a ** 2 + b ** 2 - 2 * a * b * m.cos(m.radians(angle)))
print("Given a triangle of sides {} and {}, and an angle of {}° between them, the third side is {}". format(a, b, angle, c))
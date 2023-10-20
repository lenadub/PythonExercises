# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 09:06:50 2023

@author: lena
"""

num = input("Enter a number : ")
list_num = []
sum = 0
while num != "":
    list_num.append(num)
    sum += float(num)
    num = input("Enter a number : ")
print(list_num)
moy = sum / len(list_num)
print(f"The mean is {moy}")

namestring = input("Enter the lsit of names separated by a space : ")
namelist = namestring.split()
for name in namelist:
    print(f"Hi {name}")
print(f"Welcome all {len(namelist)}")

elements = ["H","C","N","O","S","Cl"]
mass = [1.008,12.011,14.007,15.999,32.065,35.453]
total_mass = 0
for element in elements:
    n = int(input(f"How many {element} atoms are there in the molecule ? "))
    total_mass += n * mass[elements.index(element)]
print(total_mass)

n = int(input("Enter the maximum degree of the polynomial : "))
coeffs = []
function = 0
for i in range(n + 1):
    coeff = input(f"Enter the coefficient for x^{i} : ")
    coeffs.append(coeff)
x = input("Enter the value where the function is to be calculated : ")
for i in range(n + 1):
    function += float(coeffs[i]) * float(x) ** i
print(function)

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:25:59 2023

@author: lena
"""

message = "Good Morning"
print(message.count('o'))
print(message.count('ing'))
print(message.find('o'))
print(message.replace('Morning', 'Afternoon'))

print(dir(str))

num = input("Enter an integer")
num = int(num)
if num < 5 :
    print("It's less than five")
else :
    print("It's greater than or equal to five")
    
num = int(input("Enter an integer"))
if num % 2 == 0 :
    print("The number {} is an even number" . format(num))
else :
    print(f"The number {num} is an odd number")
    
marks = float((input("Enter your marks : ")))
if marks < 40 :
    print("The student has failed and got an F grade")
elif marks >= 40 and marks < 50 :
    print("The student has passed marginaly and got an E grade")
elif marks >= 50 and marks < 75 :
    print("The student has passed with a C grade")
elif marks >= 75 and marks < 90 :
    print("The student has done well and has scored a B grade")
else :
    print("The student has done excellent and passed with distinction, A grade")
    
weight = float(input("Enter your weight in kg : "))
h = input("Enter your height (e.g. 170cm, 1.70 m (the space is necessary)) : ")
height = float(h[:-2])
unit = h[-2:]
if unit == "cm" :
    height = height / 100
bmi = weight / height ** 2
print(bmi)
if bmi < 18.5 :
    print("underweight")
elif bmi >= 18.5 and bmi <25 :
    print("normal")
elif bmi >= 25 and bmi < 30 :
    print("overweight")
else : 
    print("obesity")
    
n1 = int(input("Enter a natural number : "))
n2 = int(input("Enter another natural number : "))
if n1 % n2 == 0 :
    quotient = int(n1/n2)
    print("{} is divisible by {} and the quotient is {}" . format(n1, n2, quotient))
else : 
    quotient = int(n1/n2)
    remainder = n1 % n2
    print("{} is not divisible by {} and the quotient is {} and remainder is {}" . format(n1, n2, quotient, remainder))

n1 = int(input("Enter a natural number : "))
n2 = int(input("Enter another natural number : "))
if n1 < n2 :
    print("{} is the minimum" . format(n1))
elif n1 == n2 :
    print("The 2 numbers are equal")
else :
    print("{} is the minimum" . format(n2))
    
n1 = float(input("Enter a natural number : "))
n2 = float(input("Enter a second natural number : "))
n3 = float(input("Enter a third natural number : "))
if n1 < n2 and n1 < n3:
    print("{} is the minimum" . format(n1))
elif n2 < n1 and n2 < n3:
    print("{} is the minimum" . format(n2))
elif n1 == n2 and n1 == n3:
    print("The 3 numbers are equal")
else :
    print("{} is the minimum" . format(n2))
    
unit = int(input("Enter the number of units : "))
if unit <= 100 :
    charge = 0
elif unit > 100 and unit <= 200:
    charge = 5 * (unit - 100)
else :
    charge = 500 + (unit - 200) * 10
print(charge)
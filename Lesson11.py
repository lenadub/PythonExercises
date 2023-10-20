# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:23:49 2023

@author: lena
"""
import numpy as np
import math


#Exo1
Angstroms_to_nanometers = np.linspace(1,5,21)
print(Angstroms_to_nanometers)
for i in range(len(Angstroms_to_nanometers)):
    Angstroms_to_nanometers[i] = Angstroms_to_nanometers[i] / 10
print(Angstroms_to_nanometers)

#Exo2
x0 = float(input("Enter the value of x0 : "))
s = float(input("Enter the value of s : "))
a = float(input("Enter the initial value of the x interval : "))
b = float(input("Enter the final value of the x interval : "))
n = int(input("Enter the the number of points that the table must have : "))
x = np.linspace(a, b, n)
y = np.zeros(n)
for i in range(n):
    y[i] = math.exp((-(x[i]-x0)**2)/(2 * s**2))/math.sqrt(2*math.pi)
for i in range(n):
    print("{:.3f} {:.5f}".format(x[i],y[i]))


#Exo3
temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temp_array = np.array(temp_mar)
print(f"average temp : {np.mean(temp_array)}") #We calculate the average temperature
print(f"minimum temp : {np.min(temp_array)} in {months[temp_mar.index(np.min(temp_array))]}") #We find the minimum temperature and then look for the corresponding month in the list
print(f"maximum temp : {np.max(temp_array)} in {months[temp_mar.index(np.max(temp_array))]}") #We find the maximum temperature and then look for the corresponding month in the list


#Exo4
nbstudent=int(input("Enter the number of students : "))
mat=np.zeros((nbstudent,4))
for i in range (nbstudent):
    theory=int(input("Enter the theory grade of the student : "))
    problem=int(input("Enter the problem grade of the student : "))
    totalmark=(4*theory+6*problem)/10
    mat[i,0]=i
    mat[i,1]=theory
    mat[i,2]=problem
    mat[i,3]=totalmark

print(mat)

print()

max=0
min=20
index=0
sum=0
for i in range (nbstudent):
    sum+=mat[i,3]
    if(max<mat[i,3]):
        max=mat[i,3]
        index=mat[i,0]
    if(min>mat[i,3]):
        min=mat[i,3]
print(f"The maximum total grade is : {max}. The student who got this grade is student n°{index}")
print(f"The minimum total grade is : {min}")

avg=sum/nbstudent

print(f"The average total grade is {avg}")

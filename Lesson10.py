# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:37:02 2023

@author: lena
"""

import numpy as np
import math

a = np.array([1,2,3], dtype = 'int32')
print(a)

print(a.ndim)

print(a.shape)

print(a.dtype)

print(a.itemsize)

print(a.nbytes)

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a[1,5])
print(a[1,-3])
print(a[0,:])
print(a[:,2])
print(a[0,1:-1:2])
print(a[0,:  :2])
print(np.full((2,2),99))
print(np.full_like(a,4))
print(np.random.rand(4,2))
print(np.random.randint(-4,8,size=(3,3)))
print(np.zeros((2,3)))
print(np.zeros(5))
print(np.identity(5))

arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
print(r1)

arr = np.array([[1,0,1]])
r1 = np.repeat(arr,3,axis=0)
r1[1,1] = 2
print(r1)

output = np.ones((5,5))
z = np.zeros((3,3))
z[1,1] = 9
output[1:-1,1:-1] = z
print(output)

print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a**2)

a = np.ones((2,3))
b = np.full((3,2),2)
print(np.matmul(a,b))

c=np.random.randint(-10,10, size = (4,4))
print(c)
print(np.linalg.det(c))


stats = np.array([[1,2,3],[4,5,6]])
print(np.min(stats))
print(np.max(stats,axis=0))
print(np.max(stats,axis=1))
print(np.sum(stats,axis=0))
print(np.sum(stats))

angles = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi]
angles = np.array(angles)
sin_ang = np.sin(angles)
print(f"Angles: {angles}")
print(f"Sinus: {sin_ang}")

npoints = 21
values = np.linspace(-2.0,2.0,npoints)
print(values)

y = np.arange(10,31)
y[4] = 1
print(y)

nel = int(input("Enter the number of elements in the vector : "))
lvec = []
for i in range(nel):
    comp = input(f"Enter the value of component {i} : ")
    lvec.append(float(comp))
vec = np.array(lvec)
print(vec)


nel = int(input("Enter the number of elements in the vector : "))
vec = np.zeros(nel)
for i in range(nel):
    comp = input(f"Enter the value of component {i} : ")
    vec[i] = float(comp)
print(vec)


lin = input("Enter the components of a vector in a line : ")
smooth = lin.split()
vec = np.float_(smooth)
print(f"List : {smooth}")
print(f"Vector : {vec}")


mat_A = np.zeros((3,4))
print("Matrice A")
print(mat_A)
mat_B = np.ones((5,4))
print("Matrice B")
print(mat_B)


mat = np.zeros((4,3))
for i in range(4):
    for j in range(3):
        mat[i,j] = float(input(f"Introduce the value of the element {i},{j} : "))
print(mat)

mat_A = np.zeros((2,2))
mat_B = np.zeros((2,2))
for i in range(2):
    for j in range(2):
        mat_A[i,j] = float(input(f"Introduce the value of the element {i},{j} : "))
        mat_B[i,j] = float(input(f"Introduce the value of the element {i},{j} : "))
print(mat_A)
print(mat_B)
print(mat_A@mat_B)
print(np.linalg.inv(mat_A@mat_B))
print(np.linalg.inv(mat_B)@np.linalg.inv(mat_A))

A = np.array([[1,1],[1,2]])
B = np.array([[4,1],[3,1]])
C = np.array([[24,7],[31,9]])

X = np.linalg.inv(A) @ C @ np.linalg.inv(B)
print(X)

con_list = [2.07E-5, 2.62E-7, 3.22E-5, 2.59E-4, 4.87E-5, 1.19E-4, 3.95E-5]
con_vec = np.array(con_list)
pH = np.zeros(len(con_vec))
for i in range(len(con_vec)):
    pH[i] = -math.log(con_vec[i])
print(pH)


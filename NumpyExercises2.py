# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:25:15 2023

@author: lena
"""
import numpy as np

#Exercise 1
x = np.arange(21)
x[9:16] = -x[9:16]
print(x)



#Exercise 2
x = np.arange(15, 56)
print(x[1:-1])



#Exercise 3
arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
for i in arr:
    for j in i:
        print(j, end=' ')
    print()
    
    

#Exercise 4
x = np.linspace(5, 50, 10)
print(x)



#Exercise 5
x = np.random.randint(0, 11, 5)
print(x)


#Exercise 6
x1 = np.array([1, 2, 3, 4])
x2 = np.array([5, 6, 7, 8])
x3 = x1 * x2
print(x3)



#Exercise 7
x = np.arange(10, 22)
mat = x.reshape(3, 4)
print(mat)



#Exercise 8
mat = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
nb_rows, nb_columns = mat.shape
print(f"The number of rows is : {nb_rows}")
print(f"The number of columns: {nb_columns}")



#Exercise 9
mat = np.zeros((4, 4))
mat[1::2, ::2] = 1
mat[::2, 1::2] = 1
print(mat)



#Exercise 10
arr1 = np.array([0, 10, 20, 40, 60])
arr2 = np.array([10, 30, 40])

common_values = np.intersect1d(arr1, arr2)

print("Array1:", arr1)
print("Array2:", arr2)
print("Common values between two arrays:")
print(common_values)



#Exercise 11
arr1 = np.array([10, 10, 20, 20, 30, 30])
print("Original array:")
print(arr1)

unique_elements1 = np.unique(arr1)
print("Unique elements of the above array:")
print(unique_elements1)

arr2 = np.array([[1, 1],[2, 3]])
print("Original array:")
print(arr2)

unique_elements2 = np.unique(arr2)
print("Unique elements of the above array:")
print(unique_elements2)



#Exercise 12
x1 = np.array([1, 2, 3])
x2 = np.array([4, 5, 6])
cross_product = np.cross(x1, x2)
print("Cross product:", cross_product)



#Exercise 13
cartesian_mat = np.random.rand(10, 2)

x = cartesian_mat[:, 0]
y = cartesian_mat[:, 1]
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)

print(r)
print(theta)



#Exercise 14
arr = np.arange(100)

value_to_compare = 34.99062268928913

index_closest_value = np.abs(arr - value_to_compare).argmin()
closest_value = arr[index_closest_value]

print("Original array:")
print(arr)
print("Value to compare:")
print(value_to_compare)
print("Closest value:")
print(closest_value)
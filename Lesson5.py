# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:27:41 2023

@author: lena
"""

n = int(input("Enter an integer value : "))
sum = 0
for i in range(n + 1):
    sum += i
print(f"For n = {n} the value of the sum is {sum}")

n = int(input("Enter an integer value : "))
sum = 0
for i in range(1, n + 1):
    sum += ((i + 1) / i ** 2)
print(f"For n = {n} the value of the sum is {sum : .2f}")

n = int(input("Enter an integer value : "))
prod = 1
for i in range(1, n + 1):
    prod *= i
print(f"For n = {n} the value of the factorial is {prod}")

for i in range (1,10):
    for j in range (1,10):
        print(f"{i}{j}")
        
for i in range (1,10):
    for j in range (1,10):
        if i != j :
            print(f"{i}{j}")
            
a = int(input("Enter the number of triangular numbers you want : "))
for i in range(0,a+1):
    t = i * (i + 1)/2
    print(t)
    
for i in range (0,10):
    for j in range (0,10):
        for k in range (0,10):
            print(f"{i}{j}{k}",end = ", ")

for i in range (0,10):
    for j in range (0,10):
        for k in range (0,10):
            if i+j+k == 22 :
                print(f"{i}{j}{k}",end = ", ")
                
for i in range (0,10):
    for j in range (0,10):
        for k in range (0,10):
            if i * 100 + j * 10 + k == i ** 3 + j ** 3 + k ** 3 :
                print(f"{i}{j}{k}",end = ", ")
                
n = int(input("Enter an integer value : "))
for i in range(1, n+1):
    if n % i == 0:
        print(f"{i} is a divisor of {n}")
        
n = int(input("Enter an integer value : "))
sum = 0
for i in range(0, n):
    odd = 2*i+1
    sum += odd
    print(odd)
print(f"The sum is {sum}")

n = int(input("Enter an integer value : "))
if n == 1:
    print("This number is not a prime number")
elif n > 1:
   for i in range(2,n):
       if n % i == 0:
           print("This number is not a prime number")
           break
   else:
       print("This number is a prime number")
else:
   print("This number is not a prime number")
   

fib = int(input("Enter an integer value : "))
n1=0
n2=1
count = 0
if fib <= 0:
   print("Enter a positive integer")
elif fib == 1:
   print(f"Fibonacci series upto {fib} : ")
   print(n1)
else:
   print("Fibonacci series:")
   while count < fib:
       print(n1)
       n3 = n1 + n2
       n1 = n2
       n2 = n3
       count += 1
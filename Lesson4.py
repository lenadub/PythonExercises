# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:22:55 2023

@author: lena
"""

num = int(input("Enter an integer value : "))
while num > 0 :
    res = num // 3
    print("The integer division of {} by 3 gives : {}". format(num,res))
    num = int(input("Enter an integer value :"))
print("We're done")

num = int(input("Enter an integer value : "))
ndiv = 1
while num > ndiv :
    res = num // ndiv
    print("The integer division of {} by {} gives : {}". format(num,ndiv,res))
    ndiv = ndiv + 1
print("We're done")
print("Total number of divisions : {}". format(ndiv))

num = int(input("Enter an integer value : "))
ndiv = 0
while num > 0 :
    res = num // 3
    print("The integer division of {} by 3 gives : {}". format(num,res))
    ndiv = ndiv + 1
    print("Number of divisions so far : {}". format(ndiv))
    num = int(input("Enter an integer value : "))
print("We're done")
print("Total number of divisions : {}". format(ndiv))


num = 0
count = 0
while num <= 211 :
    if num % 3 == 0 :
        count += 1
    num += 1
print("The number of numbers between 0 and 211 divisible by 3 is : {}". format(count))


num = 1
sum = 0
while num <= 10:
    sum += num
    num += 1
print (sum)


i = 0
sum = 0
while i < 10:
    num = int(input("Enter an integer value : "))
    sum += num
    i += 1
mean = sum/10
print(mean)

i = 0
num = int(input("Enter an integer value : "))
star = ""
while i < num:
    star += "*"
    print(star)
    i+=1

#Other way of doing the program above
i = 1
num = int(input("Enter an integer value : "))
while i <= num:
    print("*" * i)
    i+=1
    
num = int(input("Enter an integer value : "))
i = 1
fact = 1
while i <= num:
    fact *= i
    i+=1
print(fact)


name = "Jesaa29Roy"
size = len(name)
i=0
while i < size:
    if name[i].isdecimal():
        break
    print(name[i], end = ' ')
    i += 1
print("\nThe execution has stopped")

name = "Jesaa29Roy"
size = len(name)
i=-1
while i < size - 1:
    i += 1
    if not name[i].isalpha():
        continue
    print(name[i], end = ' ')
print("\nThe execution has stopped")


n = int(input("Enter the value of n : "))
for i in range(n):
    q_i = i**2
    print(q_i)

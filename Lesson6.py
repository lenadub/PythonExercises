# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 09:23:04 2023

@author: lena
"""

fruits = ["banana", "strawberry", "apple", "cherry", "mango", "pineapple"]
print(fruits[2])
print()

fruits.append("raspberry")
for i in fruits:
    print(i)
print()

fruits.remove("mango")
print(fruits)
print()

fruits[3]="pear"
print(fruits)
print()
    
tuple =("a", "b", "c")
#tuple.append("d")

smooth = [3.14, 7, -2+3j, 'water', False, [1, 2]]
print(smooth)
print(len(smooth))
print(smooth[5])
#print(smooth[8])
print(smooth[2:5])
print(smooth[:4])
print(smooth[1:])
print(smooth[::2])
print(smooth[5][1])
print(smooth[3][4])
print(smooth[-4:-2])
smooth.pop(5)
print(smooth)


n = int(input("Enter an integer : "))
list = []
for i in range(1, n+1):
    list.append(1/i)
print(f"{sum(list):.2f}")

line = "Temperature is 298.15 K before combustion"
words = line.split(" ")
print(words)

line = input("Enter, in a single line and SEPARATED BY SPACES, the desired temperature values : ")
smooth_txt = line.split()
print(f"List is now{smooth_txt}")
temp = []
for element in smooth_txt:
    value = float(element)
    temp.append(value)
print(f"The final list is {temp}")


a = [1, 3, 5, 7, 11]
b = [13, 17]
c = a+b
print(f"First instruction print : {c}")
b[0] = -1
d = []
for e in a :
    d.append(e+1)
print(f"Second instruction print : {d}")
d.append(b[0] + 1)
d.append(b[-1] + 1)
print(f"Third instruction print : {d}")
print(f"Fourth instruction print : {d[-2:]}")
print(f"Fifth instruction print : {d[:-1]}")
print(f"Sixth instruction print : {d[1:4]}")


n = int(input("Enter an integer : "))
list_n = list(range(n + 1))
list_n2 = []
for i in range(len(list_n)):
    list_n2.append(list_n[i] ** 2)
print(list_n2)

name = input("Enter a name : ")
grade = input("Enter a grade : ")
grades = []
names = []
sum = 0
while name != "":
    names.append(name)
    grades.append(grade)
    sum += float(grade)
    name = input("Enter a name : ")
    grade = input("Enter a grade : ")
moy = sum / len(grades)
print(f"The mean is {moy}")
for i in range(len(names)):
    print("{:14}{:5.1f}".format(names[i],float(grades[i])))

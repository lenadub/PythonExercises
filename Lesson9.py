# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:34:45 2023

@author: lena
"""

def my_function():
  print("Hello from a function")
my_function()


def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

"""def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil")"""

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))


def Max(a,b):
    if a > b:
        return a
    else:
        return b
print(Max(28,2))

def Max(list_num):
    max = -100000
    for i in list_num:
        if i > max:
            max = i
    return max
text = input("Enter 5 numbers separated by a space : ")
list_num = text.split()
for i in range(len(list_num)):
    list_num[i] = float(list_num[i])
print(Max(list_num))



#Syntax try, except, else, finally

#try : 
    #Some code
#except:
    #optional block
    #Handling of exception(if required)
#else:
    #execute if no exception
#finally:
    #Some code.....(always executed)
    
    

while True:
    try :
        num = int(input("Enter a number : "))
        if num % 2 == 0:
            print(f"{num} is Even")
            break
        else:
            print(f"{num} is Odd")
            break
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
        
"""num = int(input("Enter a number : "))
if num > 0:
    if num % 2 == 0 and num > 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")"""
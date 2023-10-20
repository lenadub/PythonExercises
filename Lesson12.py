# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:09:57 2023

@author: lena
"""

import matplotlib.pyplot as plt
import numpy as np


x=np.linspace(-2,2,101)
y = x**2
print(x)
plt.plot(x,y)
plt.show()

plt.plot(y)
plt.show()

plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(-1.5,1.5)
plt.ylim(-0.5,2.5)
plt.plot(x,y)
plt.show()

plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y, 'g', label = "x^2")
#plt.savefig("fig1.png")
y2 = x**3
plt.plot(x,y2, 'ro', label = "x^4")
y3 = x**4
plt.plot(x,y3, 'b', label = "x^4")
plt.legend()
plt.show()


x=np.linspace(0,3*np.pi,500)
plt.plot(x,np.sin(x**2))
plt.title('A simple chirp')
plt.show()


n=int(input("Enter the number of points to draw : "))
x = np.linspace(-1,1,n)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,np.cos(2*np.pi*x))
plt.title("Body function (2pix)")
plt.savefig("cos2pix.png")
plt.show()

n=int(input("Enter the number of points to draw : "))
x = np.linspace(-1,1,n)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,np.cos(2*np.pi*x), label = "cos(2pix)")
plt.plot(x,np.sin(2*np.pi*x), label = "sin(2pix)")
plt.title("Body function (2pix)")
plt.legend()
plt.savefig("trigonometric.png")
plt.show()


while True:
    try :
        n=int(input("Enter the number of points to draw : "))
        x = np.linspace(0,4,n)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.plot(x,np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp((-x)))
        plt.show()
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
        
        
n=int(input("Enter the number of points to draw : "))
T=int(input("Enter the temperature of the gas : "))
Vm = np.linspace(2,10,n)
plt.xlabel("Vm(L/mol)")
plt.ylabel("p(atm)")
p=((0.08206*T)/Vm)
plt.plot(Vm,p)
plt.title("Isotherm (ideal gas)")
plt.savefig("isotherm.jpg")
plt.show()


n=int(input("Enter the number of points to draw : "))
Vm = np.linspace(2,10,n)
nbcurves = int(input("Enter the number of curves you want : "))
for i in range(nbcurves):
    T=int(input("Enter the temperature of the gas : "))
    p=((0.08206*T)/Vm)
    plt.plot(Vm,p,label = f"{T}K")
plt.xlabel("Vm(L/mol)")
plt.ylabel("p(atm)")
plt.title("Isotherms (ideal gas)")
plt.legend()
plt.savefig("isotherms.jpg")
plt.show()



x0 = float(input("Enter the value of x0 : "))
s = float(input("Enter the value of s : "))
a = float(input("Enter the initial value of the x interval : "))
b = float(input("Enter the final value of the x interval : "))
n = int(input("Enter the number of dots to draw : "))
x = np.linspace(a, b, n)
y = np.exp((-(x-x0)**2)/(2 * s**2))/np.sqrt(2*np.pi)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gaussian function")
plt.plot(x,y)
plt.show()



n=int(input("Enter the number of points to draw : "))
x = np.linspace(0,3,n)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,np.exp(-x), label = "exp(-x)")
plt.plot(x,np.sin(3*np.pi*x)*np.exp(-x), label = "sin(3pix)*exp(-x)")
plt.title("Functions")
plt.legend()
plt.show()



n=int(input("Enter the number of points to draw : "))
a = float(input("Enter the initial value of the x interval : "))
b = float(input("Enter the final value of the x interval : "))
x = np.linspace(a, b, n)
nbcurves = int(input("Enter the number of curves you want : "))
for i in range(nbcurves):
    x0 = float(input("Enter the value of x0 : "))
    s = float(input("Enter the value of s : "))
    y = np.exp((-(x-x0)**2)/(2 * s**2))/np.sqrt(2*np.pi)
    plt.plot(x,y,label = f"x0={x0}, s={s}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gaussian function")
plt.legend()
plt.savefig("gaussianes.png")
plt.show()
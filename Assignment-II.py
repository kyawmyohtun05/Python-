# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 10:13:57 2026

@author: HP user
"""

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operation=input("Enter operation(+,-,*,/,%):")

def add(a,b):
    print("The addition is:",a+b)

def sub(a,b):
    print("The subtraction is:",a-b)

def mult(a,b):
    print("The multiplication is:",a*b)

def division(a,b):
    if b!=0:
        print("The division is:",a/b)
    else:
        print("Cannot be divided by zero!")

def modulus(a,b):
    if b!=0:
        print("The modulus is:",a%b)
    else:
        print("Cannot be divided by zero!")

if operation=="+":
    add(num1,num2)
elif operation=="-":
    sub(num1,num2)
elif operation=="*":
    mult(num1,num2)
elif operation=="/":
    division(num1,num2)
elif operation=="%":
    modulus(num1,num2)
else:
    print("Invalid operation!")
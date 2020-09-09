'''
Write a program to handle the following exceptions in you program.
           a) KeyboardInterrupt,
           b) NameError 
           c) ArithmeticError
    Note : make use of  Try, except, else: statements.

'''
#a
import time

try:
    while(True):
        time.sleep(1)
        print(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt")
#b
try:
    name = input("Enter your name:")
    print("Hello"+ name)
except NameError:
    print("NameError")

#c
try:
    c = 23/0
except ArithmeticError:
    print(" ArithmeticError ")
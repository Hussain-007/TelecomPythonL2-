'''
Create file called  "calc.py" which has following functions
i) functions to add 2 numbers
ii)  function to find diff of 2 numbers
iii) function to multiply 2 numbers
iv) all maths operations ( Sqrt, div, floor div, modulus, primnumber)
v) Fibonacci series
a) Write a new program in file "maths.py" such that you import functions of file "calc.py"
to your new program
b) Use From <module> import <function> statement to import only few function  from calc module.
'''

import math


def add(a, b):
    print("a+b: ", a + b)


def diff(a, b):
    print("a-b: ", a - b)


def multiply(a, b):
    print("a*b: ", a * b)


def sqroot(a):
    print("sqrt(a): ", math.sqrt(a))


def floor_div(a, b):
    print("a//b: ", a // b)


def division(a, b):
    print("a/b: ", a / b)


def fib_series(n):
    first = 0
    second = 1
    third = 0
    while (n > third):
        print(first, )
        first, second = second, first + second
        third += 1

def isprime(num):
    if num == 1 or num == 0 or not num%2:
        return "Not Prime"
    if num == 2:
        return "Prime"
    if num%2:
        for sub_num in range(3, num, 2):
            if not num % sub_num:
                return "Not Prime"
        else:
            return "Prime"


if __name__ == '__main__':
    n = int(input("Enter the fib Series: "))
    fib_series(n)
    n = int(input("Enter the number to check Prime: "))
    print(isprime(n))
    add(23, 15)
    diff(45, 12)
    sqroot(25)
    multiply(3, 4)
    floor_div(9, 2)
    division(5, 4)
    fib_series(10)
    print(isprime(10))
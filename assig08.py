'''
From the Standard Exception Table of Tutorials: Try implementing all (25 ) exceptions in you program.
      Note: Some exceptions might not work on your system.
'''

import math
import sys
import time

# Exception
try:
    op = 2 / b
except Exception:
    print("Exception")
# Standard error
try:
    f = open("xyz.txt", 'r')
except FileNotFoundError:
    print("Standard error:No file exists")

# Arithmetic error
try:
    a = 9 / 0
except ArithmeticError:
    print("Arithmetic error exception")

# StopIteration
try:
    f = open('output.txt', 'r', encoding='utf-8')
    for i in range(1, 100):
        print(next(f))
except StopIteration:
    print("Stop Iteration Exception")
finally:
    f.close()
# Systemexit
try:
    sys.exit()
except SystemExit:
    print("system exit exception")

# Overflow error
try:
    a = math.exp(-5 / 3 * 5251321)
except OverflowError:
    print("Overflow error exception")

# Value error
try:
    a = math.sqrt(-5 / 3)
except ValueError:
    print("ValueError")

# Overflow error
try:
    a = math.exp(-2 * 100000000000000 * 123456)
except OverflowError:
    print("overflowerrror")
# Zero division error
try:
    a = 2 / 0
except ZeroDivisionError:
    print("Zero Division exception")

# AssertionErrror
try:
    a = 123
    assert (a < 50), "assertion error"
except AssertionError:
    print("Assertion error")
# Attribute Error
try:
    raise AttributeError
except AttributeError:
    print("Attribute error")
# EOF error
try:
    f = open("output.txt", 'r', encoding='utf-8')
    f.read()
except EOFError:
    print("EOF error")

# import error
try:
    import asdf
except ImportError:
    print("Import error exception")

# look up error
dict = {'asdf': 'txt'}
try:
    print(dict['in'])
except LookupError:
    print('Lookup error')
# index error
try:
    l1 = [1, 2, 3]
    print(l1[8])
except IndexError:
    print("IndexOutofbound")

# name error:
try:
    print(d)
except NameError:
    print("Name Error")

# keyboard interrupt

try:
    x = input()
    time.sleep(5)
except KeyboardInterrupt:
    print("Keyboard interrupt")

# KeyError
try:
    print(dict['a'])
except:
    print('Key Error')

# Unbound Local Error
try:
    raise UnboundLocalError
except UnboundLocalError:
    print('UnboundLocalError!')
# IOError
try:
    f = open('asdf.txt', 'r', encoding='utf-8')
    f.write('something')
except IOError:
    print('IOError!')

# SyntaxError
try:
    raise SyntaxError
except SyntaxError:
    print('Syntax Error !')

# TypeError
try:
    a = 'string'
    a -= 2
except TypeError:
    print('Type Error')

# ValueError
try:
    a = 'string'
    print(int(a))
except ValueError:
    print('Value Error')

# Runtime Error
try:
    raise RuntimeError
except RuntimeError:
    print('Runtime Error occured !')

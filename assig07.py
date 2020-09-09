'''
Write a program to handle following exceptions using Try block.
      a) IO Error while you try writing contents into the file that is opened in read mode only.
      b) ValueError

'''
try:
    myfile = open("output.txt", "r", encoding='utf-8')
    print(myfile.read())
except IOError:
    print("Writing mode is not allowed")
#b
try:
    n = int(input("Enter value:"))
except ValueError:
    print("ValueError")

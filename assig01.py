'''
Write a program to open the existing file in read mode and perform following tasks,
a) Rad 10 character at a time and then print its current position of file object.
 Repeat this operation till the EOF.
b) Reset the file pointer after reading 100 Character from file ( Use Seek function to reset)
c) Open the file in read mode and start printing the contents from 5th line onwards.

'''
# a
myfile = open("output.txt", "r", encoding="utf8")
pointer = 0
while (True):
    c = myfile.read(10)
    if not c:
        break
    else:
        print(c)
        pointer += 10
        print(pointer)

myfile.close()
del c
# b
myfile = open("output.txt", "r", encoding="utf8")
pointer = 0
while (pointer < 100):
    c = myfile.read(10)
    if not c:
        break
    else:
        print(c)
        pointer += 10
        print(pointer)

myfile.seek(0, 0)
print(myfile.read(10))

myfile.close()
del c
# c
myfile = open("output.txt", "r", encoding='utf-8')
for i in range(5):
    myfile.readline()

for line in myfile:
    print(line)
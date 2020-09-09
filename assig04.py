'''
Open the file is read & write mode and apply following  functions
         a) All functions mentioned/covered as part of tutorial

'''


print("Enter file name to perform operations")
fname = input()
fname = 'output.txt'
f = open(fname,'rb+')
print("***Name of file-->",f.name)
print("***File descriptor no.-->",f.fileno())
print("***is file associated with terminal-->>",f.isatty())
print("***Next line1 print-->", next(f))
print("***Next line2 print-->", next(f))
f.flush()
f.close()
#
f = open(fname,'rb+')
print("***read entire file:")
print(f.read())
f.close()
#
f = open(fname,'rb+')
print("***read first five chars frm file:")
print(f.read(5))
f.close()
#
f = open(fname,'rb+')
print("***readline***->:")
print("Output of f.readline()-->",f.readline())
print("Output of f.readlines()-->",f.readlines())
f.close()
#
f = open(fname,'rb+')
f.seek(0,2)
str_input = b"Hello"
f.write(str_input)
f.seek(0,2)
seq = [b"line new1",b"line new2"]
f.writelines(seq)
f.close()
#
f = open(fname,'rb+')
print("Output after adding new line-->")
print(f.read())
f.truncate()
print("Output after truncate-->",f.readline())
f.close()
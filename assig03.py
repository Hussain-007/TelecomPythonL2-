'''
Open existing text file and reverse its contents. i.e
a) print the last line as first line and first line as last line ( Reverse the lines of the file )
b) print characters of file from last character of file till the first character of the file.
(Reverse entire contents of  file )
'''

#a
strlist = list()
for line in reversed(open("output.txt", 'r', encoding='utf-8').readlines()):
    print(line.rstrip())
    strlist.append(line.rstrip())
 #b
for string in strlist:
    print(string[::-1])
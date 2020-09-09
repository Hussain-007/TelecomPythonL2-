'''
In a given directory search all text files for the pattern "Treasure". 
       a) Find how many text file has the pattern.
       b) Count how many times pattern repeats in each file
  Note : Create at least 4 text file in a directory and keep the pattern in at least 2 files.
             Repeat the pattern in the file many times.
'''

import glob
import re


total = 0
for present in glob.glob("*.txt"):
    fh = open(present, "r", encoding='utf-8')
    strlist = fh.read().lower().split()
    for i in range(len(strlist)):
        string = re.sub(r'[?|$|.|!]', r'', strlist[i])
        strlist[i] = string
    if 'treasure' in strlist:
        print(present, strlist.count("treasure"))
        total += strlist.count("treasure")
    else:
        print(present, 0)
    fh.close()
print("Total count:", total)
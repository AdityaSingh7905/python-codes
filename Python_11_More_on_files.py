#More on files of python
#tell() function is used to know about the position of file pointer in a file
#seek() function is used to reset the position of file pointer
"""f=open("aditya.txt")
print(f.tell())
print(f.readline())
# print(f.tell())
f.seek(7)
print(f.readline())
print(f.tell())
f.close()"""
#Using with block to open files
#After using with block to open files,we didn't need close() function
# to close the file..With automatically handles this..

with open("aditya.txt") as f:
    a=f.readlines()
    print(a)
f=open("aditya.txt")
print(f.readline())
f.close()

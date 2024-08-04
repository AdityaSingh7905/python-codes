# f=open("aditya.txt","rt")
# content=f.read()
# print(content)

# content=f.read(3455)
# print("1",content)
#
# content=f.read(9)
# print("2",content)

#reading character by character of a file
# content=f.read()
# for line in content:
#     print(line)

#For printing line by line of a file
# for line in f:
#     print(line,end="")

#Readline() function
# print(f.readline())
# print(f.readline())
# print(f.readline())  #readline() reads new line character

#Storing lines of file in a list
# print(f.readlines())
# f.close()

#Writing in a file
# f=open("aditya2.txt","w")
# a=f.write("I want to become an entrepreneur")  #f.write() returns no. of characters being written
# print(a)
# f.close()
#Appending in a file
# f=open("aditya2.txt","a")
# f.write("Also, I want to become a good software engineer\n")
# f.close()
#For reading and writing both in a file
f=open("aditya.txt","r+")
print(f.read())
f.write("\nHe studied in Jawahar Navodaya Vidyalaya.")
# print(f.read())
f.close()

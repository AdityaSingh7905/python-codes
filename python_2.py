#String Slicing in python
mystr = "aditya is a good boy"
print(mystr)  #prints the whole string
#print(mystr[0])   #indexing starts from 0 to length -1
#print(mystr[5])
#print(len(mystr))  #len() is used to calculate length of the string..In c, we use strlen()
#print(mystr[0:5])  # 0 is including while 5 is excluding
#print(mystr[:6])  # automatically assumes 0 at the beginning of the indexing
#print(mystr[0:])  # automatically assumes end of the string
#print(mystr[78])  # shows error when indexing is out of range
#print(mystr[0:78])
#print(mystr[::2])  # if you want to skip letters of the string
#print(mystr[::])   # By default , sipping index ko 1 assume kar leta hai
#print(mystr[0:20:3])  # Above line of code gives the same output as that we get from the same line code
#  NEGATIVE INDEXING IN A STRING
""" 012345678910111213141516171819
    Aditya is  a   g o o d   b o y
                  -8-7-6-5-4-3-2-1  """ # negative indexing starts from -1 to -length
#print(mystr[-4:-2])
"""How to reslove negative indexing?? 
   We have to replace negative index with the positive index of the word of the string"""
#print(mystr[16:18])
#print(mystr[::-1])  # prints inverse of the string
#print(mystr[::-50])  # firstly inverse the string and then skip letters of the string
# Python functions for strings
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("boy"))
print(mystr.capitalize())
print(mystr.count("is"))
print(mystr.find("is"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is","are"))
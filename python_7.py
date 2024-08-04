#For loop
#list=["Harry","Larry","Carry","Marie"]
#for item in list:
    #print(item)
#=[list2=[["Aditya",18],["Anshuman",14],["Simmi",16]]  # Lists of list
"""for item in list2:
    print(item)
for item,age in list2:
    print(item,"and age is",age)"""
#Creating a dictionary
"""dict1=dict(list2)
for item,age in dict1.items():
    print(item,age)
for item in dict1:
    print(item)"""
#QUIZZES
list=["Aditya",3,5,8,"Anshuman",13,"Akhil","Anniruddha",7]
for item in list:
    if str(item).isdigit() and item>6:
        print(item)

#While loop
"""i=0
while(i<45):
    print(i)
    i=i+1"""
#Break and continue statements
"""i=0
while(True):
    if i+1<5:
        i=i+1
        continue
    print(i+1,end=" ")
    if i==44:
        break
    i=i+1"""
#QUIZZES
"""while(1):
    num=int(input())
    if num<=100:
        continue
    print("Congratulations!You printed a number greater thean 100")"""
while(1):
    num=int(input("Enter the number\n"))
    if num>100:
        print("Congratulations!You printed a number greater thean 100\n")
        break
    else:
        print("Try Again!\n")
        continue



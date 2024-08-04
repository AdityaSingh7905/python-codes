#Lambda functions are also called Anonymous functions..
#Lambda functions are basically one liner functions.
def add(x,y):
      return x+y
#Making lambda function of the above function
# add=lambda x,y: x+y
# print(add(5,4))

# def minus(x,y):
#     return x-y
#Lambda functions
# minus = lambda x,y: x-y
# print(minus(9,4))

# def a_first(a):
#     return a[1]
# a=[[1,14],[5,6],[8,23]]
# # a.sort(key=a_first)
# a.sort(key=lambda x:x[1])
# print(a)
#While importing modules , we are using its functions.Sometimes,there are sub-modules inside modules
#so,we use sub-modules functions for our usage..
import random
num=random.randint(0,100)#randint function generates random integer numbers between 0 and 100 including them
# print(num)
num1=random.random()*100#Random function generates random number b/w 0 and 1
#After multipling with 100, it generates numbers b/w 0 and 100
# print(num1)
list=["Aditya","anshuman","simmi","ashu","krish"]
choice=random.choice(list)
print(choice)
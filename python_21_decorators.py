"""Function can be in a variable """
# def func1():
#     print("Subscribe now")
#
# func=func1
# del func1
# func()

# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a=funcret(1)
# print(a)
"""Function can be passed as an arguments"""
# def executor(func):
#     func("Aditya Singh")
#  executor(print)
# """Function returned by a function"""
# def create_adder(x):
#     def adder(y):
#         return x+y
#     return adder
# add=create_adder(15)
# print(add(10))
"""______________________________DECORATORS_______________________"""
def decor1(func):
    def inner1():
        x=func()
        return x*x
    return inner1
def decor(func):
    def inner():
        x=func()
        return 2*x
    return inner
# @decor1
# @decor
def num():
    return 10
num=decor1(decor(num))
# decor=decor1(decor)
# num=decor(num)
a=num()
print(a)

#DEcorators are used to modify the behaviour of a function ,without modifying the structure of the function..
"""def hello_decorator(func):
    def inner1():
        print("This is before function execution..")
        func()
        print("This is after the function execution..")
    return inner1
def function_to_be_used():
    print("This is inside the function..")

function_to_be_used=hello_decorator(function_to_be_used)
function_to_be_used()"""


#Functions are pieces of codes that do a particular task or job for the programmer
"""There are two types of functions:
1) Built-in functions  # Already implemented in python interpreter
2) User-defined functions  # Created by the user or programmer for the sake of its convenience"""
# Built-in functions
a=8
b=88
c=sum((a,b))
print(c)
# User defined functions
# def keyword is used for indicating user defined functions.
def func1(a,b):
    """This function is used to calculate average of two numbers.
    It will not calculate average of three numbers"""
    average=(a+b)/2
    print(average)
    print("Hello!you are in func1.")
    return average
#func1()
#print(func1())  # None is printed because the function does not return anything
print(func1(7,8))
print(func1.__doc__)  #Docstrings basically gives information about the function
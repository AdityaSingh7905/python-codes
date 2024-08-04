numbers=["3","34","64"]
# numbers[2]=numbers[2]+1
# for item in list:
#     item=int(item)
# for i in range(len(numbers)):
#     numbers[i]=int(numbers[i])
# numbers[2]=numbers[2]+1
# print(numbers[2])
"""There is another way of doing the above segment of code..Use map function."""
# numbers=list(map(int,numbers))
# print(numbers)
# numbers[2]=numbers[2]+1
# print(numbers)
"""Using lambda function along with map function.."""
# def sq(x):
#     return x*x
# num=[2,3,5,6,76,3,2]
# square=list(map(sq,num))
# print(square)
#By Using lambda function
# square=list(map(lambda x:x*x,num))
# print(square )
# def square(x):
#     return x*x
# def cube(x):
#     return x*x*x
# func=[square,cube]
# for i in range(5):
#     val=list(map(lambda x:x(i),func))
#     print(val)
#____________________________FILTER FUNCTION________________________________
# list_1=[1,2,3,4,5,6,7,8,9]
# def is_greater_5(num):
#     return num>5
# print(is_greater_5(7))
# gr_than_5=list(map(is_greater_5,list_1))
# gr_than_5=list(filter(is_greater_5,list_1))
# print(gr_than_5)
#___________________________REDUCE FUNCTION_________________________________
#It is a part of functools module.By using all these functions , performance improvement increases
from functools import reduce
list1=[1,2,3,4,5]
# num=0
# for i in list1:
#     num=num+i
# print(num)
num=reduce(lambda x,y:x*y,list1)
print(num)
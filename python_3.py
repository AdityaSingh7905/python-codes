# List and its functions
grocery = ["Harpic","Lifebuoy","Surfexcel","Vimbar","Chocolate",56]
#print(grocery[3])
numbers = [2,9,7,13,11]
numbers.sort()
numbers.reverse()
print(numbers)
#print(numbers[::-1])
# List functions in python
print(len(numbers))
print(min(numbers))
print(max(numbers))
numbers.append(15)
numbers.append(17)
print(numbers)
numbers.insert(2,10)
print(numbers)
numbers.remove(2)
print(numbers)
num = [2,4,6]
numbers.extend(num)  # add element to the last of the list
print(numbers)
numbers.pop()
print(numbers)
numbers.append(2)
print(numbers.count(4))  # prints no. of occurences of particular value in a list
print(numbers.index(4))  # prints index position of specified value
num2 = numbers.copy()   # Copy all elements of the existing list into a new one
print(num2)
numbers.clear()  # Clear all the existing elements of the list
print(numbers)
num2[1]=98
print(num2)
# Tuple is similar like list but it is immutable ie non changeable
tp = (1,2,3)
print(tp)
#tp[1]=4
#print(tp)
# Swapping of two numbers
a=1
b=8
"""temp=a
a=b
b=temp"""
#print(a,b)
# In python , it can be done by
a,b = b,a
print(a,b)

#Try Except exception Handling
num1=input("Enter the number 1:\n")
num2=input("Enter the number 2:\n")
try:
   print("Sum of these two numbers is:",int(num1)+int(num2))
except Exception as e:
    print(e)

print("This line is very important!!")
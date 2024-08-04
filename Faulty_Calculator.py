num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number:"))
op = input("Enter your operator:")
dict={"45*3":"555","56+9":"77","56/6":"4"}
if num1==45 and num2==3 and op=='*':
    print(num1,op,num2,"=",dict["45*3"])
elif num1==56 and num2==9 and op=='+':
    print(num1,op,num2,"=",dict["56+9"])
elif num1==56 and num2==6 and op=='/':
    print(num1,op,num2,"=",dict["56/6"])
elif op=='+':
    print(num1,op,num2,"=",num1+num2)
elif op=='-':
    print(num1,op,num2,"=",num1-num2)
elif op=='*':
    print(num1,op,num2,"=",num1*num2)
elif op=='/':
    print(num1,op,num2,"=",num1/num2)
elif op=='**':
    print(num1,op,num2,"=",num1**num2)
elif op=='%':
     print(num1,op,num2,"=",num1%num2)
else:
    print("Error:Check your numbers again")
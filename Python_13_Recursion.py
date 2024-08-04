#When a function calls itself inside its body, it is called as recursion..
#Factorial of a number n is given by: fac(n)=n*(n-1)*(n-2)*(n-3).........*3*2*1
#fac(n)=n*fac(n-1)
#Iterative Approach
def factorial_iterative(n):
    fac=1
    for i in range(n):  #this loop will run from i=0 to i=n-1
        fac=fac*(i+1)
    return fac
#Recursive Approach
def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
# for n=5 recursive factorial can be explained by-
"""  fac(5)=5*fac(4)
     fac(5)=5*4*fac(3)
     fac(5)=5*4*3*fac(2)
     fac(5)=5*4*3*2*fac(1)
     fac(5)=5*4*3*2*1 = 120
"""
num=int(input("Enter the number for which you want to calculate factorial:\n"))
print("Iterative factorial:",factorial_iterative(num))
print("Recursive_factorial:",factorial_recursive(num))

#QUIZZES OF THE DAY
#Write code for fibonacci series
def fibonacci_recursive(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)
#for n=5 :
""" 5=finonacci_recursive(4)+fibonacci_recursive(3)
    5=finonacci_recursive(3)+fibonacci_recursive(2)+fibonacci_recursive(2)+fibonacci_recursive(1)
    5=fibonacci_recursive(2)+fibonacci_recursive(1)+fibonacci_recursive(1)+fibonacci_recursive(0)+fibonacci_recursive(1)+fibonacci_recursive(0)+1
    5=fibonacci_recursive(1)+fibonacci_recursive(0)+1+1+0+1+0+1
    5=1+0+4
    fibonacci(5)=5
   """


number=int(input("Enter the number:\n"))
print(fibonacci_recursive(number))


#Global scope ,Global variable and Global Keyword
#Global keyword is used to change value of global variable inside any local function
x=89  # Global variable
def harry():
    x=20  #Local variable of function harry()
    def rohan():
        global x
        x=88
    print("before calling rohan()",x)
    rohan()
    print("after calling rohan()",x)

harry()
print(x)








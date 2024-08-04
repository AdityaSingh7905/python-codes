class A:
    classvar1="I am a class variable in A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="Instance var in class A"
        self.special="Special"
class B(A):
    # classvar1="I am in class B"
    def __init__(self):
        # super().__init__()
        self.var1="I am inside class B's constructor"
        self.classvar1="Instance var in class B"
        super().__init__()
        # a.__init__()
        print(super().classvar1)
        print(A.classvar1)
        print(B.classvar1)
"""Pahle vo B me instance variable find karega..agar nhi mila tab class 
 A me instance variable find karega , agar nhi mila tab Class B me 
 Class variable find karega and if not found then it will try Class
 variable in CLass A.."""

a=A()
b=B()
print(b.special,b.var1,b.classvar1)
# print(b.var1,b.classvar1)
class A:
    def met(self):
        print("Aditya Singh is in Class A")

class B(A):
    def met(self):
        print("Aditya Singh is in Class B")
class C(A):
    def met(self):
        print("Aditya Singh is in Class C")
class D(B,C):
    pass
    # def met(self):
    #     print("Aditya Singh is in Class D")
class D(C,B):
    pass
    # def met(self):
    #     print("Aditya Singh is in Class D")

a=A()
b=B()
c=C()
d=D()
d.met()
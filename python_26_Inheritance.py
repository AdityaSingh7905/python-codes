class Employee:
    no_of_leaves=10
    no_of_holidays=45
    def __init__(self,name,salary,post):
        self.name=name
        self.salary=salary
        self.post=post
    def printdetails(self):
        return (f"This is {self.name} having salary {self.salary} and my post is {self.post}..")

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    """Class Method as a alternate constructor"""
    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("We are using a Static Method if we do not require instances and class variables.."+"This is written by "+ string)

adi=Employee("Aditya Singh",100000,"Assitant Manager")
# print(adi.printdetails())
#
# karan=Employee.from_str("Karan Singh-20000-Secretary")
# print(karan.printdetails())
# karan.printgood("Aditya Singh")

class Programmer(Employee):
    # no_of_holidays=56
    def __init__(self,name,salary,post,languages):
        self.name=name
        self.salary=salary
        self.post=post
        self.language=languages
    def printprog(self):
        return f"This is Programmer named {self.name} having salary {self.salary} and his post is {self.post}.The languages he know is {self.language}"

aditya=Programmer("Aditya Singh",200000,"Manager",["C","C++","Python"])
print(aditya.printprog())
print(aditya.no_of_leaves)
print(aditya.no_of_holidays)
class Employee:
    no_of_leaves=10
    def __init__(self,name,salary,post):
        self.name=name
        self.salary=salary
        self.post=post
    def printdetails(self,string):
        return (f"This is {self.name} having salary {self.salary} and my post is {self.post}.."+string)

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
print(adi.printdetails("Aditya Singh"))

karan=Employee.from_str("Karan Singh-20000-Secretary")
print(karan.printdetails("Karan Singh"))
karan.printgood("Aditya Singh")

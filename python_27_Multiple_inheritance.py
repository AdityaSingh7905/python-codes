class Employee:
    no_of_leaves=10
    var=8
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
class Player:
    no_of_games=4
    var=9
    def __init__(self,name,games):
        self.name=name
        self.game=games
    def printdetails(self):
        return f"This is {self.name} and he plays {self.game}"
"""__________________MULTIPLE INHERITANCE____________________"""
class CoolProgrammer(Employee,Player): #Order matters here while writing the base class
    var=10
    language="C++"
    def printlanguage(self):
        print(self.language)

adi=Employee("Aditya Singh",100000,"Assitant Manager")
aditya=CoolProgrammer("Aditya Singh",200000,"Charter Accountant")
print(aditya.printdetails())
print(aditya.var)



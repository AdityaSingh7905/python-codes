class Employee:
    no_of_leaves=10
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
        # params=string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
adi=Employee("Aditya Singh",100000,"Assitant Manager")
print(adi.printdetails())
adi.change_leaves(34)
print(adi.no_of_leaves)
print(Employee.no_of_leaves)


karan=Employee.from_str("Karan Singh-20000-Secretary")
print(karan.printdetails())

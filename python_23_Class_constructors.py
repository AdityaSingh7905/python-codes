class Employee:
    no_of_Leaves=10
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"This is {self.name} having salary {self.salary} and my role is {self.role}"

adi=Employee("Aditya Singh",200000,"Manager")
# print(adi.printdetails())
adi.no_of_Leaves=100
print(adi.no_of_Leaves)  #Pahle ye instance variable find karta hai tab class variable me jata hai
class Employee:
    # Dunder Methods
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def printdetails(self):
        return f"This is {self.name} having salary of {self.salary} and he is {self.role}"
    def __add__(self, other):
        return self.salary+other.salary
    def __truediv__(self, other):
        return self.salary/other.salary
    # This is called Operator Overloading
    def __repr__(self):
        return f"Employee('{self.name}',{self.salary},'{self.role}')"
    def __str__(self):
        return f"This is {self.name} having salary of {self.salary} and he is {self.role}"


emp1=Employee("Aditya Singh",345,"Programmer")
emp2=Employee("Anshuman Singh",200,"Student")
print(emp1+emp2)
print(emp1/emp2)
print(repr(emp1))
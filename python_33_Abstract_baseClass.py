#from abc import ABCMeta,abstractmethod
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def printdetails(self):
        return 0

class Rectangle(Shape):
    type="Rectangle"
    sides=4
    def __init__(self):
        self.length=6
        self.breadth=4
    def printdetails(self):
        return self.length*self.breadth
rec1=Rectangle()
print(rec1.printdetails())
Obj=Shape()
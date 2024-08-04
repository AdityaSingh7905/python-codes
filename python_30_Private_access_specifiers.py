"""The members of the class that are declared private are accessible within the class only,
private access modifier is the most secure access modifier."__" is used to create private data members
 and private member functions......"""
class Geek:
    #Constructor
    def __init__(self,name,roll,branch):
        #Private data members
        self.__name=name
        self.__roll=roll
        self.__branch=branch
    #Private member function
    def __displayDetails(self):
        #accessing private data members
        print("Name:",self.__name)
        print("Roll:",self.__roll)
        print("Branch:",self.__branch)
    #Public member function
    def accessPrivateFunction(self):
        #accessing private member function
        self.__displayDetails()
#Creating object
obj=Geek("Aditya Singh","21/11/EE/011","Electronics and Communication Engineering")
obj.accessPrivateFunction()
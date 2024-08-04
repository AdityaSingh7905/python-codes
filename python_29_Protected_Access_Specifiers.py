class Student:
    #Constructor
    def __init__(self,name,roll,branch):
        #Protected Data Members
        self._name=name
        self._roll=roll
        self._branch=branch
    #Protected Member function
    def _displayRollAndBranch(self):
        #Accessing protected data members
        print("Roll:",self._roll)
        print("Branch:",self._branch)

#Derived class
class Geek(Student):
    # def __init__(self,name,roll,branch):
    #     Student.__init__(self,name,roll,branch)

    #public member function
    def displayDetails(self):
        #accessing protected data members of super class
        print("Name:",self._name)
        #accessing protected member functions of the super class
        self._displayRollAndBranch()
#Creating objects of the derived class
obj=Geek("Aditya Singh","21/11/EE/011","Electronics and Communication Engineering")
obj.displayDetails()
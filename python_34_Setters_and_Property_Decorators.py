class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{self.fname}.{self.lname}@gmail.com"

    def explian(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname=="None" or self.lname=="None":
            return "Email is not set.Please try using setter.."
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("Setting now..")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname="None"
        self.lname="None"

Aditya_Singh=Employee("Aditya","Singh")
Anshuman_Singh=Employee("Anshuman","Singh")
print(Aditya_Singh.explian())
print(Aditya_Singh.email)
Aditya_Singh.fname="ADITYA"
print(Aditya_Singh.email)

Aditya_Singh.email="aditya.singh@codewithharry.com"
print(Aditya_Singh.email)
print(Aditya_Singh.fname)
print(Aditya_Singh.lname)

del Aditya_Singh.email
print(Aditya_Singh.email)
"""--------------------------------OBJECT INTROSPECTION---------------------------------------"""
# print(type(Aditya_Singh))
# # print(type("This is an apple"))
# print(id(Aditya_Singh))
# print(dir(Aditya_Singh))
# """Inspect Module is use for Object Introspection"""
# import inspect
# print(inspect.getmembers(Aditya_Singh))
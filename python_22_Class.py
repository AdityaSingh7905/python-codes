class Employee():
    no_of_leaves=8
    pass

harry=Employee()
rohan=Employee()

harry.name="Harry Nagar"
harry.salary=50000
harry.post="Chartar Accountant"
rohan.name="Rohan Chaddha"
rohan.salary=10000
rohan.post="Mechanic"
print(harry.name,harry.post,harry.no_of_leaves)
print(Employee.no_of_leaves)
Employee.no_of_leaves=10
print(Employee.no_of_leaves)  #Class variables can be changed only by accessing class not by object..
# But Object instances can be changed by object accessing
print(Employee.__dict__)
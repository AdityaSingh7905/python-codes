# Creating a set
# Set is an unordered collection of data types
s=set()  # Empty set having no elements
#print(type(s))
l=["Aditya","Anshuman","Akhil"]
s1=set(l)
#print(s1)
#print(type(s1))
#Adding elements in the set
s.add(1)
#s.add(1)   #still it is showing only {1},not {1,1} as duplicate elements are not allowed in the set
s.add(2)
s.add(3)
s.add(4)
print(s)
#For removal of elements from the set
s.remove(3)
print(s)
#s.remove(2)
#print(s)
print(len(s))
print(max(s))
print(min(s))
#Using set properties
print(s.union({1,2,3,5}))  #Union
print(s.intersection({1,2,3,5}))  #Intersection
print(s.isdisjoint({1,2,5}))
print(s.isdisjoint({5,6,7}))  #For checking if the two sets are disjoint ie no elements are commom in them
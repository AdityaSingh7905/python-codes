#  Dictionary and its functions
#  Dictionary is a collection of key:values pairs,used to store data values like a map
d1={}  # empty dictionary
#print(type(d1))
d2={1:"Aditya",2:"Anshuman",3:"Akhil",4:"Akash"}
#print(d2[2])
d3={1:"Mathematics",2:"English",3:{"Science":"Physics","Social":"History"}}  # Nested dictionary
#print(d3[3]["Science"])
# Adding elements in the dictionary
d3[4]="Hindi"
d3[5]="Computerscience"
#print(d3)
d3[3]["Games"]="PhysicalEducation"
#print(d3)
# Removing elements from the dictionary
#d4=d3   # Actually,both d3 and d4 are pointers pointing to the same dictionary so
        # if we delete any element using d4 pointer it reflects in the d3 as well..Remember no copying is done here
#del d4[1]
#print(d3)
# For copying of the elements of the dictionary
d4=d3.copy()
del d4[1]
#print(d3)  # here copying is done therefore no deletion of d4 is reflected in the d3
# We can also access elements of the dictionary using get() function
print(d3.get(3))
# We can also update elements of the dictionary using update() function
d3.update({6:"Malyalam"})
d3.update({3:"Science"})
#print(d3)
print(d3.keys())  # prints all the keys of the dictionary
print(d3.values())  #  prints all the values of the dictionary
print(d3.items())  #  prints all the elements of the dictionary
#d3.pop(1)  # removes value of specfied key
#d3.popitem()   # removes last inserted key-value pair
d3.clear()    # clear all the elements of the dictionary
print(d3)
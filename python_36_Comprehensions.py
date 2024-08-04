# Comprehensions refers to easy and concise way to construct new sequences using already defined sequences
#There are four types of comprehensions in python
#List Comprehension
ls=[i for i in range(1,100) if i%3==0]
print(ls)

#Dictionary Comprehensions
dict={i:f"item{i}" for i in range(1,101) if i%20==0}
print(dict)
#It is also used to reverse key value pair easily
dict1={values:key for key,values in dict.items()}
print(dict1)

#Set Comprehensions
s={item for item in ["dress1","dress2","dress1","dress1","dress2","dress2"]}
print(s)

#Generators Comprehensions
evens=(i for i in range(1,101) if i%5==0)
print(type(evens))
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())

for i in evens:
    print(i)
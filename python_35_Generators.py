#iterable  __iter__() or __getitem__()
#Iterator  __next__()
#Iteration

# Genrators  - one time callable iterators
def gen(n):
    for i in range(n):
        yield i  # the state of the function is frozen once yield is encountered

g=gen(3)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())

for i in g:
     print(i)

h="harry"
for c in h:
    print(c)

# h="harry"
h=34567
ier=iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
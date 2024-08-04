import pickle
#Pickling is a process in which a python object is converted into a byte stream
cars=["Audi","BMW","Maruti Suzuki","Ferarri"]
with open("aditya4.txt",'wb') as f:
    pickle.dump(cars,f)


print(pickle.dumps(cars))
# print(pickle.loads(cars))
p=pickle.dumps(cars)
print(pickle.loads(p))

with open("aditya4.txt",'rb') as f1:
    print(pickle.load(f1))
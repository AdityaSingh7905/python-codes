# def function_names_print(a,b,c,d,e,f):
#     print(a,b,c,d,e,f)
# function_names_print("Harry","Aditya","Anshuman","Akash","Akhil","Shivam")

def funargs(normal,*args,**kwargs):  #args accept arguments as a tuple
    print(normal)
    for item in args:
        print(item)
    print("\nSome of them are our heroes.Those students are:")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

names=["Harry","Aditya","Anshuman","Riya","Pranjal","Abhinav"]
normal="These are our students:"
kw={"Harry":"Monitor","Aditya":"House Captain","Anshuman":"Games Captain"}
funargs(normal,*names,**kw)
# a=input("What is your name:")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed.")
#
# print(f"Hello {a}")

# a=int(input("What is your salary:"))
# b=int(input("How much you spend from ur salary:"))
# if b==0:
#     raise ZeroDivisionError("We are stopping as b is equal to 0.")
#
# print(a/b)

c=input("Enter your name:")
try:
    print(a)
except Exception as e:
    if c == "harry":
        raise ValueError("Harry is blocked , he is not allowed.")
    print("Exception handled..")
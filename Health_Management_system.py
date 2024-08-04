#HEALTH MANAGEMENT SYSTEM FOR TRACKING DIET PLAN AND EXERCISE PLAN OF INDIVIDUAL
def getdate():
    import datetime
    return datetime.datetime.now()

def load():

    a=int(input("Press 1:(for Harry),Press 2:(for Aditya),Press 3:(for Anshuman)2 to load data:\n"))
    b=int(input("Press 1:(for diet plan),Press 2:(for exercise plan):\n"))
    if a==1:
        if b==1:
            print("Welcome ! in Harry's diet plan..")
            with open("Harry_diet.txt","a") as f:
                f.write("\n[")
                f.write(str(getdate()))
                f.write("]\t")
                f.write(input())

        else:
            print("Welcome ! in Harry's exercise plan..")
            with open("Harry_exercise.txt","a") as f:
                f.write("\n[")
                f.write(str(getdate()))
                f.write("]\t")
                f.write(input())
    elif a==2:
        if b==1:
            print("Welcome ! in Aditya's diet plan..")
            with open("Aditya_diet.txt","a") as f:
                f.write("\n[")
                f.write(str(getdate()))
                f.write("]\t")
                f.write(input())
        else:
            print("Welcome ! in Aditya's exercise plan..")
            with open("Aditya_exercise.txt","a") as f:
                f.write("\n[")
                f.write(str(getdate()))
                f.write("]\t")
                f.write(input())
    else:
        if b==1:
            print("Welcome ! in Anshuman's diet plan..")
            with open("Anshuman_diet.txt","a") as f:
                f.write("\n[")
                f.write(str(getdate()))
                f.write("]\t")
                f.write(input())
        else:
            print("Welcome ! in Aditya's exercise plan..")
            with open("Aditya_exercise.txt","a") as f:
                f.write("\n[")
                f.write(str(getdate()))
                f.write("]\t")
                f.write(input())

def retrieve():
    a = int(input("Press 1:(for Harry),Press 2:(for Aditya),Press 3:(for Anshuman) to retrieve data:\n"))
    b = int(input("Press 1:(for diet plan),Press 2:(for exercise plan):\n"))
    if a == 1:
        if b == 1:
            print("Welcome ! in Harry's diet plan..")
            with open("Harry_diet.txt", "r") as h:
                print(h.read())
        else:
            print("Welcome ! in Harry's exercise plan..")
            with open("Harry_exercise.txt", "r") as f:
                print(f.read())
    elif a == 2:
        if b == 1:
            print("Welcome ! in Aditya's diet plan..")
            with open("Aditya_diet.txt", "r") as f:
                print(f.read())
        else:
            print("Welcome ! in Aditya's exercise plan..")
            with open("Aditya_exercise.txt", "r") as f:
                print(f.read())
    else:
        if b == 1:
            print("Welcome ! in Anshuman's diet plan..")
            with open("Anshuman_diet.txt", "r") as f:
                print(f.read())
        else:
            print("Welcome ! in Aditya's exercise plan..")
            with open("Aditya_exercise.txt", "r") as f:
                print(f.read())

print("Press 1:(for loading data),Press 2:(for retrieving data):\n")
inp=int(input())
if inp==1:
    load()
else:
    retrieve()

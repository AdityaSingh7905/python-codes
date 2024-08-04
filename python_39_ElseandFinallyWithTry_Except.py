f=open("Harry_diet.txt")

try:
    f1=open("file2.py")

except Exception as e:
    print(e)

else:
    print("Else will run if and only if except will not run..")

finally:  # Used for Code Cleanup
    print("Run this anyway..")
    f.close()
    # f1.close()

print("Important Stuff..")



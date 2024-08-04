""" Star Pattern """
n=int(input("Enter the value of n:\n"))
a=int(input("Enter the value of boolean variable//either 1 or 0:\n"))
i=0
while(i<n):
    if a==1:
      j=0
      while(j<=i):
        print("*",end="")
        j=j+1
      print()
    else:
      k=n
      while(k>i):
         print("*",end="")
         k=k-1
      print()
    i=i+1
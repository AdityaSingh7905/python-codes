import time
initial=time.time() #time function inside time module calculates number of ticks used by the program
print(initial)
i=0
while(i<5):
    print("Aditya is a good boy.")
    i+=1
print("WHILE loop ran in",time.time()-initial,"seconds.")

initial2=time.time()
print("\n",initial2)
for i in range(5):
    print("Aditya is a good boy.")
print("FOR loop run in",time.time()-initial2,"seconds.")

"""Time.time function calculates number of ticks..
   time.local function convert this ticks returned by time function into local time.
    As,time.localtime function return a tuple.Therefore ,time.asctime is used to convert tuple into normal 
    representataion form.."""
localtime=time.asctime(time.localtime(time.time()))
print(localtime)
time.sleep(5) # time.sleep function is used to stop working of a program for few moments..
print(localtime)
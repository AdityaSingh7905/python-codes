# import time
# from functools import lru_cache
# @lru_cache(maxsize=4)
# def some_work(n):
#     #Some task taking n seconds
#      time.sleep(n)
#      return n
# if __name__ == '__main__':
#     print("Now running some work")
#     some_work(3)
#     some_work(1)
#     some_work(6)
#     some_work(2)
#     print("Done...Calling again")
#     input()
#     some_work(3)
#     print("Called again..")

#__________________________________FIBONACCI SERIES USING FUNCTION CACHING__________________________________
from functools import lru_cache
#fibonacci series with lru cache
@lru_cache(maxsize=4)
def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print("Going to print fibonacci series..")
print(fibonacci(60))
print("Taking to much time to print..Let's use lru cache..then it will save our time.")
print(fibonacci(60))

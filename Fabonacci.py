#!/usr/bin/python3
from functools import lru_cache
fibonacci_cache={}

@lru_cache(maxsize=1000)
def  fibonacci(n):
    #if we have cached the value,then return it
    #if n in fibonacci_cache:
        #return fibonacci_cache[n]
    
    
    #compute the Nth term
    if n ==1:
        return 1
    elif n==2:
        return 1
    elif n >2 :
        return fibonacci(n-1)+fibonacci(n-2)

    #cache the value and return it
    #fibonacci_cache[n] = value
    #return value


for n in range(1,1000):
    print(n, ":", fibonacci(n))


import time

def factorial_while(n):
    ret = n
    while(n>1):
        n-=1
        ret = ret * n
    return ret

def factorial_for(n):
    ret = n
    for i in range(1, n):
        ret = ret * i
    return ret

def factorial_rec(n):
    if(n == 1):
        return 1
    else:
        return n * factorial_rec(n-1)
#


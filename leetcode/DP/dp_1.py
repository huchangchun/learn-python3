#encoding=utf-8
import os,time
def fib(N):
    if N == 1 or N == 2:
        return 1
    else:
        return fib(N-1) + fib(N-2)
def fib2(N):
    if N < 1:
        return 0
    global arr
    arr = [0] * (N+1)
    return helper(N)
def helper(N):
    if N == 1 or N==2:
        return 1
    if arr[N] != 0:
        return arr[N]
    arr[N] = helper(N-1) + helper(N-2)
    return arr[N]

def fib_dp(N):
   
    if N==0:
        return 0
    if N==1 or N==2:
        return 1
    arr = [0] * (N+1)
    arr[1] = arr[2] = 1
    for i in range(3,N+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[i]

def fib_dp2(N):
   
    if N==0:
        return 0
    if N==1 or N==2:
        return 1
    prev = 1
    curr = 1
    for i in range(3,N+1):
        cursum = prev + curr
        prev = curr
        curr = cursum
    return curr
    
if __name__== "__main__":
     
 
    
    st = time.time()
    print(fib2(35))
    print("cost:",time.time() - st)    
    st = time.time()
    print(fib_dp(35))
    print("cost:",time.time() - st)      
    
    st = time.time()
    print(fib_dp2(35))
    print("cost:",time.time() - st)          
    
    st = time.time()
    print(fib(35))
    print("cost:",time.time() - st)    
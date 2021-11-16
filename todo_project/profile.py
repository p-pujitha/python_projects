import time
def profile_count(skip_recursion=False):
    def decorator(func):
        if not skip_recursion:
            def inner(n):
                inner.count += 1
                return func(n)
        else:
            def inner(n):
                def subinner(n):
                    return func(n)

                if inner.rec:
                    inner.rec = False
                    res = subinner(n)
                    inner.rec = True
                    return res
                else:
                    inner.count += 1
                    inner.rec = True
                    return func(n)
        inner.count = 0
        inner.rec = True
        return inner

    return decorator

def profile_time(func):
    time0=time.clock()
    def inner1(n):
        inner1.total_time+=(time.clock()-time0)
        return func(n)
    inner1.total_time=0
    return inner1



@profile_count
def fib1(n):
     if n==0 or n==1:
         return n
     else:
         return fib1(n-1)+fib1(n-2)



@profile_time
def fib3(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib3(n - 1) + fib3(n - 2)




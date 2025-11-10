#@function
def fib_r(n:int)-> int:
    #@variant n
    return n if 1 >= n else fib_r(n-1)+fib_r(n-2)

r = fib_r(0)
#@assert r==0
r = fib_r(1)
#@assert r==1
r = fib_r(2)
#@assert r==1
r = fib_r(3)
#@assert r == 2
r = fib_r(4)
#@assert r == 3

# contre exemple
r = fib_r(3)
#@assert r != 5
r = fib_r(4)
#@assert r != 7
r = fib_r(5)
#@assert r != 13


def m_fib(n:int)->int:
    #@requires n >=1
    #@ensures result==fib_r(n)
    fn = 1
    fp = 0
    i = 1
    while i <= n-1:
       #@variant n-i
       #@invariant 1 <= i <= n
       #@invariant fp == fib_r(i-1)
       #@invariant fn == fib_r(i)
       fn, fp, i = fn + fp, fn, i+1
    return fn
          

# r = m_fib(0)
# #@assert r==0
r = m_fib(1)
#@assert r==1
r = m_fib(2)
#@assert r==1
r = m_fib(3)
#@assert r == 2
r = m_fib(4)
#@assert r == 3

# contre exemple
r = m_fib(3)
#@assert r != 5
r = m_fib(4)
#@assert r != 7
r = m_fib(5)
#@assert r != 13

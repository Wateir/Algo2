#@function
def power(n:int,m:int)-> int:
  #@requires m >= 0
  #@variant m
  return 1 if m == 0 else n*power(n,m-1)

#@function
def pow_sqr(x,y)-> int:
  #@requires x>=0
  #@requires y>=0
  #@ensures power(power(x,2),y) == power(x,2*y)
  pass
  
def expR(A:int, B:int)-> int:
  #@requires B>=0
  #@ensures result == power(A,B)
  x,y = A,B
  z = 1
  while (y>0):
    #@variant y
    #@invariant z*power(x,y)==power(A,B)
    #@invariant B>=y
    if (y%2 == 0):
      #@assert z*power(x*x,y//2) == power(A,B)
      x,y = x*x, y//2
      #@assert z*power(x,y) == power(A,B)
    else:
      #@assert (z*x)*power(x,y-1) == power(A,B)
      z,y = z*x, y-1
      #@assert z*power(x,y) == power(A,B)
  return z
  
r = power(2,4)
#@assert r == 16
r = power(3,3)
#@assert r == 27
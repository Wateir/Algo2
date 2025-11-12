def div_mod(a:int,b:int)->Tuple[int, int]:
    #@requires b>0
    #@ensures forall q,r. (q,r)== result -> a == q*b+r and 0<= r < b
    pass
  
r = div_mod(5,3)
#@assert r == (1,2)
r = div_mod(2,2)
#@assert r == (1,0)
r = div_mod(17,5)
#@assert r == (3,2)
r = div_mod(24,5)
#@assert r == (4,4)
r = div_mod(1,4)
#@assert r == (0,1)
 
# contre exemples
r = div_mod(7,5)
#@assert r != (2,-2)
r = div_mod(14,4)
#@assert r != (3,1)
def Cube1(n:int) -> int:
    #@requires n>= 0
    #@ensures result==n*n*n
    pass

def Cube(n:int) -> int:
    #@requires n>=0
    #@ensures result ==n*n*n
    i, c, k = n, 0, 1
    while (i > 0):
        #@variant i
        #@invariant c==(n-i)*(n-i)*(n-i)
        #@invariant n>=i>=0
        #@invariant k==3*(n-i)*(n-i)+3*(n-i)+1
        c = c+k
        k = k+(6*(n-i))+6
        i = i-1
    return c
    

import sys
print(sys.getrecursionlimit())


sys.setrecursionlimit(30000)

def A (m , n,i=0):
    if ( m ==0):
        return (n +1, i)
    if ( n ==0):
        a, i = A (m-1,1, i+1)
        return(a, i)
    a, i = A(m,n-1, i+1)
    return A (m -1 ,a , i +1)

print(A(3,1))

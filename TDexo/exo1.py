def puiss(X,i):
    res = 1
    while i!= 0:
        res = X * res
        i-=1
    return res

print(puiss(2,3))

def poly (A,X,i=0):
    if len(A)== 1:
        return 1[0]*puiss(X,i)
    else:
        return A[0]*puiss(X,1)+ poly(A[1:],X,i+1)

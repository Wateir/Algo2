def moy(T,m,i):
    if len(T)==1:
        return(i+1)
    else:
        return(i)
    elif T[0]>=m:
        return(moy(T[O:]))

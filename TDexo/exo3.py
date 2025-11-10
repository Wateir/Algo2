tab = [1,2,2,3,4,5]
def retourne(array):
    if len(array) == 1:
        return(array)
    return(retourne(array[1:]+[array[0]]))
print(retourne(tab))

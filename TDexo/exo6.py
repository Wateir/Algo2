def BHaut ( n ):
    if (n >0):
        print ( n * '*')
        BHaut (n -1)

def BBas ( n ):
    if (n >1):
        BBas (n -1)
        print ( n * '*')

def parm(n):
  BHaut(n)
  BBas(n)
  
parm(5)

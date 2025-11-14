def recherche_partie(a:int)-> int:
  #@requires a>0
  #@ensures result*result <= a < (result+1)*(result+1)
  if ((a//2)*(a//2) == a):
    return a
  elif ((a//2)*(a//2) < a):
    return recherche_partie(a//2)
  else:
    return recherche_partie((a+1)//2)
  
r = recherche_partie(1)
#@assert r == 1
r = recherche_partie(8)
#@assert r == 2
r = recherche_partie(13)
#@assert r == 3
r = recherche_partie(36)
#@assert r == 6
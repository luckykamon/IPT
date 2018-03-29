def suiteu(n):
  c = 0.5
  for i in range(n):
    c = 2 - c/4.
  return c

def suitev(n):
  c = 0
  for i in range(n):
    c = 1-c*c/2.
  return c

def suiterecur(f,a,n):
  c = a
  for i in range(n):
    c = f(c)
  return c

def somme(l):#somme des elements d'une liste l
  s = 0
  n = len(l)  #len comme length
  for i in range(n): #parcours par indice
    s = s + l[i]
  return s

def somme(l):
  s = 0
  for v in l:#parcours par valeur
    s = s + v
  return s

def produit(l):
  s = 1
  for v in l:#parcours par valeur
    s = s * v
  return s
  
def minimum(l):
  c = l[0]
  for v in l:
    if v<c:
      c = v
  return c










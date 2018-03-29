def suiteu(n):
  c = 1
  for k in range(n):
    c = c*c*0.25
  return c

def recur2(n):#avec un compteur a intermediaire
  c = 1
  d = 3
  for k in range(n):
    a = d
    d = d - 2 * c
    c = a
  return c

def recur2(n):
  c,d=1,3
  for k in range(n):
    c,d = d,(d-2*c)
  return c

def recherche(l,a):
  c = False
  for v in l:
    c = c or v==a
  return c

def recherche(l,a):#permet de s'arreter si on rencontre a
  for v in l:
    if v==a:
      return True
  return False

def nombre(l,a):
  c = 0
  for v in l:
    if v==a:
      c = c + 1
  return c

def premier(n):
  c = 2
  while n%c != 0:
    c = c + 1
  return c == n

def premier(n):#on s'arrete a la racine carree
  c = 2
  while n%c != 0 and c*c <= n:
    c = c + 1
  return c*c > n

def somme(l):
  s = 0
  for v in l:
    s = s + v
  return s

def ppe(l):
  m = l[0]
  for v in l:
    if v < m:
      m = v
  return m

def ind_ppe(l):
  ind = 0
  for i in range(1,len(l)):
    if l[i] < l[ind]:
      ind = i
  return ind




  
   

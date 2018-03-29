def recherche1(l,a):
  b = False
  for v in l:
    b = b or v==a
  return b

def recherche2(l,a):
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

def nb_el1(l):#cardinal de l'ensemble des valeurs
  n = 0
  m = len(l)
  for k in range(m):
    i = 0
    while i<k and l[i]!=l[k]:
      i = i + 1
    if i == k:
      n = n + 1
  return n

def nb_el2(l):
  m=[]
  for v in l:
    if not recherche2(m,v):
      m.append(v)
  return len(m)

def card_max1(l):#element avec la plus grande occurrence
  m = 0
  a = l[0]
  for v in l:
    if nombre(l,v)>m:
      m = nombre(l,v)
      a = v
  return a,m

def card_max2(l):#element avec la plus grande occurrence
  m = 0
  a = l[0]
  for v in l:
    x = nombre(l,v)
    if x>m:
      m = x
      a = v
  return a,m


def card_max3(l):
  m1=[]#valeurs distinctes
  m2=[]#nb d'occurrences pour ces valeurs
  for v in l:
    if not recherche2(m1,v):
      m1.append(v)
      m2.append(nombre(l,v))
  ind_max = 0
  for k in range(len(m2)):
    if m2[k]>m2[ind_max]:
      ind_max = k
  return m1[ind_max],m2[ind_max]

    











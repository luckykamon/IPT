
'''fonctions canoniques
def somme(l):
  s = 0
  for v in l:
    s = s + v
  return s
def somme(l):
  s = 0
  for i in range(len(l)):
    s = s + l[i]
  return s
'''

def somme(c,a):
  s = 0
  for i in range(len(c)):
    if a[i]:
      s = s + c[i]
  return s

def estReussie(c,a,Obj):
  return somme(c,a) >= Obj

def estStable(c,a,Obj):
  s = somme(c,a)
  if s < Obj:
    return False
  for i in range(len(c)):
    if a[i] and s - c[i]>= Obj:
        return False
  return True

def allianceMin(c,Obj):
  n = len(c)
  s = 0
  a = [False] * n
  for k in range(1,n+1):
    if s >= Obj:
      return a
    a[-k] = True
    s = s + c[-k]
  if s >= Obj:
    return a
  raise ValueError
 
def allianceMin(c,Obj):
  n = len(c)
  s = 0
  a = [False] * n
  for k in range(-1,-n-1,-1):
    if s >= Obj:
      return a
    a[k] = True
    s = s + c[k]
  if s >= Obj:
    return a
  raise ValueError     

def allianceMin(c,Obj):
  n = len(c)
  s = 0
  a = [False] * n
  k = n-1
  while s < Obj and k>=0:
    a[k] = True
    s = s + c[k]
    k = k-1
  if s >= Obj:
    return a
  raise ValueError   

def suivanteDe(a):
  n = len(a)
  k = 0
  while k<n and a[k]:
    a[k] = False
    k = k+1
  if k<n:
    a[k] = True
    return False
  return True

def listeStables(c,Obj):
  n = len(c)
  l = []
  a = [False] * n
  while not suivanteDe(a):
    if estStable(c,a,Obj):
      l.append(a)#probleme avec les modifications de listes
  return l
  
def listeStables(c,Obj):
  n = len(c)
  l = []
  a = [False] * n
  while not suivanteDe(a):
    if estStable(c,a,Obj):
      print a

def cumuls(c):
  n = len(c)
  t=[0] * n
  s = 0
  for k in range(n):
    s = s + c[k]
    t[k] = s
  return t

def cumuls(c):
  n = len(c)
  t=[0] * n
  t[0]= c[0]
  for k in range(1,n):
    t[k] = t[k-1] + c[k]
  return t
  



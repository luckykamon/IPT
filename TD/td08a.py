#QUESTION 1
'''
def recherche(l,a):
  for v in l:
    if v == a:
      return True
  return False
'''
def admet_point_fixe(t):
  for k in range(len(t)):
    if t[k] == k:
      return True
  return False

#QUESTION 2
'''
def somme(l):
  s = 0
  for v in l:
    s += v
  return s
def nb_occur(l,a):
  s = 0
  for v in l:
    if v == a:
      s += 1
  return s
'''
def nb_points_fixes(t):
  s = 0
  for k in range(len(t)):
    if t[k] == k:
      s += 1
  return s  

#QUESTION 3
'''
def composee(f,k,x):
  y = x
  for i in range(k):
    y = f(y)
  return y
#correspond aux suites definies par recurrence
'''
def itere(t,k,x):
  y = x
  for i in range(k):
    y = t[y]
  return y

#QUESTION 4
def nb_points_fixes_iteres(t,k):
  s = 0
  for i in range(len(t)):
    if itere(t,k,i) == i:
      s += 1
  return s

#QUESTION 5
#1. L'orbite d'un element est au plus de cardinal n
#donc un point fixe, s'il est atteint, le sera 
#au plus tard a la (n-1)eme iteree.
#2. S'il existe un attracteur principal, alors
#c'est le seul point fixe.

def admet_attracteur_principal(t):#version rapide
  n = len(t)
  pt_fixe = False
  for k in range(n):
    if t[k] == k:
      z = k
      pt_fixe = True
      break
  if not pt_fixe:
    return False   
  n = len(t)
  for x in range(n):
    if not itere(t,n-1,x) == z:
      return False
  return True
      
def admet_attracteur_principal(t):#version desirable
  n = len(t)
  #recherche de point fixe et verification de l'unicite
  pt_fixe = False
  for k in range(n):
    if t[k] == k:
      if pt_fixe:
        return False
      else:
        z = k
        pt_fixe = True
  if not pt_fixe:
    return False
  #verification pour chaque x dans t
  for x in range(n):
    y = x
    for k in range(1,n):
      y = t[y]
      if y == z:
        break
      if k == n-1:
        return False
  return True

#QUESTION 6

def temps_de_convergence(t,x):
  temps = 0
  y = x
  while y != t[y]:
    temps += 1
    y = t[y]
  return temps

#QUESTION 7
def tmax(t):
  n = len(t)
  a = [True]*n
  b = [0]*n
  for x in range(n):
    if a[x] and a[t[x]]:
      a[a[x]] = False
      b[x] = b[x] + 1













    

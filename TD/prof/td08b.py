'''
def recherche(l,a):
  for v in l:
    if v == a:
      return True
  return False
'''

def admet_points_fixes(l):
  for k in range(len(l)):
    if l[k] == k:
      return True
  return False

'''
def somme(l):
  s = 0
  for v in l:
    s = s + v
  return s
def nb_occurences(l,a):
  s = 0
  for v in l:
    if v == a:
      s = s + 1
  return s
'''
def nb_points_fixes(l):
  s = 0
  for k in range(len(l)):
    if t[k] == k:
      s = s + 1
  return s

'''
def composee(f,k,x):
  a = x
  for i in range(k):
    a = f(a)
  return a
'''
def itere(t,x,k):
  a = x
  for i in range(k):
    a = t[a]
  return a

def nb_points_fixes_iteres(t,k):
  s = 0
  for x in range(len(l)):
    if itere(t,x,k) == x:
      s = s + 1
  return s

def nb_points_fixes_iteres(t,k):
  t_k = [itere(t,x,k) for x in range(len(t))]
  return nb_points_fixes(t_k)

'''
si t admet un attracteur principal, il est alors unique et c'est l'unique point fixe de t.
le temps de convergence d'une valeur est inferieure ou egale a n, car les orbites sont incluses dans En et sont donc de longueur maximale n'''

def admet_attracteur_principal(t):
  n = len(t)
  t_n = [itere(t,x,n) for x in range(n)]
  return t_n == [t_n[0] for x in range(n)]
#complexite en Theta(n^2)

def temps_de_convergence(t,x):
  temps = 0
  a = x
  while a != t[a]:
    temps = temps + 1
    a = t[a]
  return temps
  
def temps_max(t):
  n = len(t)
  liste_temps = [-1] * n
  for k in range(n):
    if liste_temps[k] == -1:
      orbite = [k]
      j = k
      while t[j] != j and liste_temps[j] == -1:
        j = t[j]
        orbite.append(j)
      n_orb = len(orbite)-int(liste_temps[j] != -1)
      for i in range(n_orb):
        liste_temps[orbite[i]] = liste_temps[j]+n_orb-i
  return liste_temps      
        
      










    

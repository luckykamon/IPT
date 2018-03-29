t1=[1,3,5,7,9,1,3,5,7,9]
t2=[5,5,2,2,0,2,2]

def admet_point_fixe(t):
  for k in range(len(t)):
    if k==t[k]:
      return True
  return False

def nb_points_fixes(t):
  n=0
  for k in range(len(t)):
    if k==t[k]:
      n+=1
  return n

def itere(t,x,k):
  for i in range(k):
    x=t[x]
  return x

def nb_points_fixes_iteres(t,k):
  n=len(t)
  l=[0]*n
  for i in range(n):
    l[i]=itere(t,i,k)
  return nb_points_fixes_iteres(l)

def admet_attracteur_principal(t):
  p=True
  s=False
  n=len(t)
  for i in range(n):
    if i==t[i]:
      for k in range(n):
        for j in range(n):
          if itere(t,t[k],j)==i:
            s=True
        p=p and s
        s=False
      if p:
        return True
  return False

def temps_de_convergence(t,x):
  n=len(t)
  if x==t[x]:
    return 0
  for i in range(n):
    if t[x]==x:
      return i
    x=t[x]

def temps_de_convergence_max(t):
  p=0
  for j in range(len(t)):
    if temps_de_convergence(t,j)>p:
      p=temps_de_convergence(t,j)
  return p

def est_croissante(t):
  for k in range(len(t)-1):
    if t[k]>t[k+1]:
      return False
  return True

def point_fixe(t):
  for k in range(len(t):
    if t[k]==k:
      return k



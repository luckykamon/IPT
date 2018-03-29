'''QUESTION 1'''

#avec des append
def somme(p,q):
  l = []
  n,m = len(p),len(q)
  if n <= m:
    for k in range(n):
      l.append(p[k]+q[k])
    for k in range(n,m):
      l.append(q[k])
  else:
    for k in range(m):
      l.append(p[k]+q[k])
    for k in range(m,n):
      l.append(p[k])
  return l

#en modifiant les valeurs de l, une fois par indice
def somme(p,q):
  n,m = len(p),len(q) 
  if n <= m:
    l = [0] * m
    for k in range(n):
      l[k] = p[k]+q[k]
    for k in range(n,m):
      l[k] = q[k]
  else:
    l = [0] * n
    for k in range(m):
      l[k] = p[k]+q[k]
    for k in range(m,n):
      l[k] = p[k]
  return l

#en modifiant les valeurs de l, en parcourant p puis q
def somme(p,q):
  n,m = len(p),len(q)
  l = [0] * max(n,m)
  for k in range(n):
    l[k] = p[k]
  for k in range(m):
    l[k] += q[k]
  return l

#par comprehension
def somme (p,q):
  n,m = len(p),len(q)
  mini = min(n,m)
  l1 = [p[k]+q[k] for k in range(mini)]
  l2 = [p[k] for k in range(mini,n)]
  l3 = [q[k] for k in range(mini,m)]
  return l1+l2+l3

'''QUESTION 2'''
#on ne parcourt pas suivant l, mais suivant p et q
def produit(p,q):
  n, m = len(p), len(q)
  l = [0] * (n + m - 1)
  for k in range(n):
    for j in range(m):
      l[k+j] += p[k] * q[j]
  return l

'''QUESTION 3'''
def prod_ext(la,p):
  return [la * v for v in p]

'''QUESTION 4'''
def eval_pol(p,x):
  s = 0
  a = 1
  for k in range(len(p)):
    s += p[k] * a
    a *= x
  return s

'''QUESTION 5'''

def pol_lag(x,y):
  n = len(x)
  s = []
  for k in range(n):
    l = [1]
    for j in range(n):
      if j != k:
        q = 1./(x[k]-x[j])
        l = produit(l, [-x[j] * q, q] )
    s = somme(s,prod_ext(y[k],l) )
  return s

import matplotlib.pyplot as plt
def graph(f,a,b,x):#x liste des abscisses de coincidence
  #creation du polynome
  y = [f(t) for t in x]
  p = pol_lag(x,y)
  #creation des listes pour plt
  X = [a+(b-a)*v/1000. for v in range(1000)]
  Y1 = [f(t) for t in X]
  Y2 = [eval_pol(p,t) for t in X]
  #creation des objets graphiques
  plt.plot(X,Y1)
  plt.plot(X,Y2)
  #trace
  plt.show()
  
  
  






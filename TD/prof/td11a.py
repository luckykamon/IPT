#QUESTION 1

#avec des append
def somme(p1,p2):
  l = []
  n1,n2 = len(p1),len(p2)
  if n1 <= n2:
    for k in range(n1):
      l.append(p1[k]+p2[k])
    for k in range(n1,n2):
      l.append(p2[k])
  else:
    for k in range(n2):
      l.append(p1[k]+p2[k])
    for k in range(n2,n1):
      l.append(p1[k])
  return l
#en rajoutant d'abord p1 puis p2 a un polynome nul
def somme(p1,p2):
  n1,n2 = len(p1),len(p2)
  maxi = max(n1,n2)
  l = [0] * maxi
  for k in range(n1):
    l[k] = p1[k]
  for k in range(n2):
    l[k] += p2[k]
  return l
  
#par comprehension
def somme(p1,p2):
  n1,n2 = len(p1),len(p2)
  mini = min(n1,n2)
  return [p1[k]+p2[k] for k in range(mini)] + [p1[k] for k in range(mini,n1)] + [p2[k] for k in range(mini,n2)]


#QUESTION 2

#avec un nombre lineaire d'ecritures dans la liste
def produit(p1,p2):
  n1,n2 = len(p1),len(p2)
  l = [0] * (n1+n2-1)
  for k in range(n1+n2-1):
    s = 0
    for i in range(max(0,k-(n2-1)),min(k,n1-1)+1):
      s += p1[i] * p2[k-i]
    l[k] = s
  return l

#avec un nombre quadratique d'ecritures dans la liste
def produit(p1,p2):
  n1,n2 = len(p1),len(p2)
  l = [0] * (n1+n2-1)
  for i in range(n1):
    for j in range(n2):
      l[i+j] += p1[i] * p2[j]
  return l
  
#QUESTION 3
def prod_ext(p,la):
  return [la*v for v in p]

#QUESTION 4
def eval_pol(p,x):
  s = 0
  a = 1
  for k in range(len(p)):
    s += p[k] * a
    a *= x
  return s

#QUESTION 5
def pol_lag(X,Y):
  n = len(X)
  l = [0]
  for i in range(n):
    lag = [1]
    for j in range(n):
      if j!=i:
        q = 1./(X[i]-X[j])
        lag = produit(lag,[-X[j]*q,q])
    l = somme(l, prod_ext(lag,Y[i]) )
  return l

#QUESTION 6
import matplotlib.pyplot as plt

def graph(f,X,xmin,xmax):
  val = [f(x) for x in X]
  poly = pol_lag(X,val)
  pas_graph = (xmax-xmin)*1./1000
  subfine = [xmin + k *pas_graph for k in range(1000)]
  Y1 = [f(x) for x in subfine]
  Y2 = [eval_pol(poly,x) for x in subfine]
  plt.plot(subfine,Y1)
  plt.plot(subfine,Y2)
  plt.show()

#QUESTION 7
def pol_prim(p):
  return [0]+[p[k]/(k+1.) for k in range(len(p))]

def integ_pol(p,a,b):
  q = pol_prim(p)
  return eval_pol(q,b)-eval_pol(q,a)




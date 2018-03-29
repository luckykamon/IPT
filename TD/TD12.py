def somme(p1,p2):
  n1,n2 = len(p1),len(p2)
  mini = min(n1,n2)
  return [p1[k]+p2[k] for k in range(mini)] + [p1[k] for k in range(mini,n1)] + [p2[k] for k in range(mini,n2)]


def produit(p1,p2):
  n1,n2 = len(p1),len(p2)
  l = [0] * (n1+n2-1)
  for i in range(n1):
    for j in range(n2):
      l[i+j] += p1[i] * p2[j]
  return l
  
def prod_ext(p,la):
  return [la*v for v in p]

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

def quadrature(X):
  n=len(X)
  l=[0]
  lk=[]
  for i in range(n):
    lag=[1]
    for j in range(n):
      if j!=i:
        q = 1./(X[i]-X[j])
        lag = produit(lag,[-X[j]*q,q])
    lk.append(integ_pol(lag,-1.,1.))
  return lk

def f(x):
  return 2*x+1

def integ_cano(f,x,l):
  s=0
  for k in range(len(x)):
    s+=l[k]*f(x[k])
  return s

def integ_quad(f,a,b,x):
  s=0
  l=quadrature(x)
  for k in range(len(x)):
    s+=l[k]*f((a+b)/2.+(x[k])*(a-b)/2.)
  return ((b-a)/2.)*s



import matplotlib.pyplot as plt
def somme(p1,p2):
  if len(p1)>len(p2):
    n=len(p1)
  else:
    n=len(p2)
  s=[0]*n
  for k in range(len(p1)):
    s[k]=s[k]+p1[k]
  for j in range(len(p2)):
    s[j]=s[j]+p2[j]
  return s

def produit(p1,p2):
  n=len(p1)+len(p2)
  s=[0]*(n-1)
  for k in range(len(p1)):
    for j in range(len(p2)):
      s[k+j]=s[k+j]+p1[k]*p2[j]
  return s

def prod_ext(l,p1):
  for k in range(len(p1)):
    p1[k]=l*p1[k]
  return p1

def eval_pol(x,p1):
  s=0
  for k in range(len(p1)):
    s=s+p1[k]*x**k
  return s

def pol_lag1(x,y):
  l1=[1]*len(x)
  l2=[1]*len(x)
  for k in range(len(l1)):
    for j in range(len(l1)):
      if j!=k:
        l1[k]=produit([l1[k]],[-x[j],1])
        l2[k]=l2[k]*(x[k]-x[j])
  for d in range(len(l1)):
    l1[d]=prod_ext(1*1./(l2[d]),l1[d])
  p=[0]
  print(l1)
  for e in range(len(l1)):
    l1[e]=prod_ext(y[e],l1[e])
  for f in range(len(l1)):
    p=somme(p,l1[f])
  return p

def pol_lag2(X,Y):
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

def graph(x,y):
  X = [k for k in range(6)]
  Y1 = [eval_pol(X,pol_lag2(x,y)) for n in X]
  plt.plot(X,Y1)
  plt.show()

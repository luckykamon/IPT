P=[2,3]
Q=[4,-5]
def polynomenul(P):
  for i in P:
    if i!=0:
      return False
  return True

def degre(P):
  for i in range(1,len(P)):
    if P[-i]!=0:
      return len(P)-1
  return 0

def derivee(P):
  n = len(P)
  l = []
  for i in range(1,n):
    l.append( P[i]*i )
  return l

def somme(P,Q):
  n=len(P)
  m=len(Q)
  l=min(n,m)
  R=[]
  for i in range(l):
    R.append(P[i]+Q[i])
  if n>m:
    for i in range(l,n):
      R.append(P[i])
  else:
    for i in range(l,m):
      R.append(Q[i])
  return R

def produit(P,Q):
  n=len(P)
  m=len(Q)
  R=[0]*(n+m-1)
  for i in range(n):
    for v in range(m):
      R[i+v]=R[i+v]+P[i]*Q[v]
  return R


C=[(-1,3),(1,0),(3,15),(2,13)]
def degre_c(C):
  m=0
  for i in range(len(C)):
    if C[i][1]>m:
      m=C[i][1]
  return m


def coefficient_c(p,i):
  m=0
  for v in range(len(p)):
    if p[v][1]==i:
      return p[v][0]
  return 'pas de coefficient de degre i'

def somme_c

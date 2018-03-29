def f(n):
  u = 1
  for i in range(n):
    u = u*u/4.
  return u


def recur(n):
  u=1
  v=3
  w=0
  if n>1:
    for i in range(n-1):
      w = v - 2*u
      u = v
      v = w
    return w
  if n==1:
    return 3
  if n==0:
    return 1

def recur2(n):
  a,b=1,3
  for k in range (n):
    a,b=b,b-2*a
  return a


l=[15,17,3,5,2]
def recherche(l,a):
  c = False
  for v in l:
   c = c or a==v
  return c
  

def recherche2(l,a):
  c = 0
  for v in l:
    if a==v:
      c=c+1
  return c

from math import sqrt
def premier(p):
  c=2
  while p%c != 0:
      c=c+1
      if c>sqrt(p):
        return True
  return False
    

s=0
def somme(l):
  s=0
  for v in l:
    s = s + v
  return s
    



def petit(l):
  p=l[0]
  n=0
  for k in l:
    if p>l[n]:
      p=l[n]
    n=n+1
  return p


def nbel(l):
  m=l[0]
  n=0
  for k in l:
    recherche(l,k)
    if c=True
      m=







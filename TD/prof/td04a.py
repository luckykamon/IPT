# -*- coding: utf-8 -*-

def f1(x):
  return x*x-2
lambda x:x*x-2


def racine_dichot(f,a,b,eps):
  if f(a)==0:
    return a
  if f(b)==0:
    return b
  if f(a)*f(b)>0:
    return 'methode non applicable'
  x = a
  y = b
  while y-x>eps:#on suppose a<b
    z = (x+y)/2.
    if f(z)==0:
      return z
    if f(x)*f(z)>0:
      x = z
    else:
      y = z
  return x

def recherche_dichot(l,a):
  n = len(l)
  if a<l[0] or a>l[n-1]:
    return False
  if a == l[0] or a == l[n-1]:
    return True
  i1 = 0
  i2 = n-1
  while i2>i1+1:
    i3 = (i1+i2)//2
    if a ==l[i3]:
      return True
    if a>l[i3]:
      i1 = i3
    else:
      i2 = i3
  return a == l[i1] or a == l[i2]

def insere_dichot(l,a):
  n = len(l)
  if a<=l[0]:
    l = [a]+l
    return l
  if a>=l[n-1]:
    l.append(a)
    return l
  i1 = 0
  i2 = n-1
  while i2>i1+1:
    i3 = (i1+i2)//2
    if a == l[i3]:
      l = l[:i3]+[a]+l[i3:]
      return l
    if a>l[i3]:
      i1 = i3
    else:
      i2 = i3
  if a == l[i1]:
    l = l[:i1]+[a]+l[i1:]
    return l
  l = l[:i2]+[a]+l[i2:]
  return l
    
  
  
  
  

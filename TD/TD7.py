import numpy as np
import matplotlib.pyplot as plt

a=np.array([False,True,True,True])
c=np.array([10,12,14,15])
Obj=42

def somme(c,a):
  s=0
  for i in range(len(a)):
    if a[i]:
      s=s+c[i]
  return s

def estReussie(c,a,Obj):
  return somme(c,a)>=Obj

def estStable(c,a,Obj):
  s=[]
  l=0
  if estReussie(c,a,Obj)==False:
    return False
  for i in range(len(a)):
    if a[i]:
      s.append(c[i])
  for k in range(len(s)):
    l=l+s[k]
  for j in range(len(s)):
    if l-s[j]>=Obj:
      return False
  return True

def AllianceMin(c,Obj):
  n = len(c)
  a = [False]*n
  s = 0
  k = n-1
  while s < Obj and k>=0:
    s = s+ c[k]
    a[k] = True
    k = k - 1
  if s < Obj:
    raise ValueError
  return a

def suivanteDe(a):
  for k in range(len(a)):
    if not a[k]:
      a[k] = True
      return True
    else:
      a[k]=False
  return False      

def imprimer(a):
  for k in range(len(a)):
    if a[k]==1:
      print k

def binaire(a):
  return sum([int(a[k]) * (2**k) for k in range(len(a))])


def AlliancesStables(c,Obj):
  a = [False]*len(c)
  l = []
  while suivanteDe(a):
    if estStable(c,a,Obj):
      l.append(binaire(a))
  return l



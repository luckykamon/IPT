import math
from math import sin
from math import *
import numpy as np
import matplotlib.pyplot as plt

def evol(x,y,h,g,m,l,c):
  return(x+h*y,y+h*(-(g*1./l)*sin(x)-(c*1./m)*y))

def sol_num1(pos0,vit0,t,n,g,m,l,c):
  d=[0]*(n+1)
  d[0]=(pos0,vit0)
  for k in range(1,n+1):
    d[k]=evol(d[k-1][0],d[k-1][1],t*1./n,g,m,l,c)
  return d

def sol_num2(pos0,vit0,t,n,g,m,l,c):
  d=[(pos0,vit0)]
  for k in range(1,n+1):
    d.append(evol(d[k-1][0],d[k-1][1],t*1./n,g,m,l,c))
  return d

def sol_num_np(pos0,vit0,t,n,g,m,l,c):
  return 0

def pendule_TX(pos0,vit0,t,n,g,m,l,c):
  X=[sol_num1(pos0,vit0,t,n,g,m,l,c)[j][0] for j in range(n)]
  T=[k*t*1./n for k in range(n)]
  plt.plot(T,X)
  plt.show()

def pendule_XY(pos0,vit0,t,n,g,m,l,c):
  X=[sol_num1(pos0,vit0,t,n,g,m,l,c)[j][0] for j in range(n)]
  Y=[sol_num1(pos0,vit0,t,n,g,m,l,c)[j][1] for j in range(n)]
  plt.plot(X,Y)
  plt.show()

def espace_phases(posmin,posmax,p,vit0,t,n,g,m,l,c):
  for k in range(p):
    pos0=posmin+k*(posmax-posmin)*1./p
    X=[sol_num1(pos0,vit0,t,n,g,m,l,c)[j][0] for j in range(n)]
    Y=[sol_num1(pos0,vit0,t,n,g,m,l,c)[j][1] for j in range(n)]
    plt.plot(X,Y)
  plt.show()

def coeff_inconnu():
  l=1
  m=1
  t=3
  vit0=0
  g=9,81
  pos0=pi*1./2
  posmax=pi*1./3
  eps=0.01
  c=5
  a=0
  b=10
  maxi=0
  while not -posmax-eps<maxi<-posmax+eps:
    for k in range(50):
      if sol_num1(pos0,vit0,t,50,g,m,l,c)[k][0]<maxi:
        maxi=sol_num1(pos0,vit0,t,50,g,m,l,c)[k][0]
    #a finir

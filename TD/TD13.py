import numpy as np
import matplotlib.pyplot as plt
from math import sin

f= lambda x: sin(x)

def riemann(f,t0,t,y0,n):
  r=0
  for k in range(n):
    c=t0+k*(t-t0)*1./n
    r=r+f(c)
  return y0+((t-t0)*1./n)*r

def primitive(f,t0,tmax,y0,n):
  r=0
  l=[0]*(n+1)
  for k in range(n):
    l[k]=(y0+((tmax-t0)*1./n)*r)
    c=t0+k*(tmax-t0)*1./n
    r=r+f(c)
  l[n]=(y0+((tmax-t0)*1./n)*r)
  return l

def fonction_et_derivee(f,t0,tmax,y0):
  n=1000
  T=np.linspace(t0,tmax,n)
  Y1=[f(x) for x in T]
  Y2=primitive(f,t0,tmax,y0,n-1)
  plt.plot(T,Y1)
  plt.plot(T,Y2)
  plt.show()

def sol_autonome(f,t,y0,n):
  h=t*1./n
  a=y0
  for k in range(n):
    a+=h*f(a)
  return a

def euler(f,t1,y0,n):
  l = [y0]
  h = t1*1./n
  for k in range(n):
    l.append( l[-1] + h * f(l[-1]) )
  return l

def evol_et_sol_auto(f,t1,y0,n):
  T = [t1*k*1./n for k in range(n+1)]
  Y2 = euler(f,t1,y0,n)
  a,b = min(Y2),max(Y2)
  Y = [a+k*1./n*(b-a) for k in range(n+1)]
  Y1 = [f(y) for y in Y]  
  plt.plot(Y1,Y)
  plt.plot(T,Y2)
  plt.show()

def comparaison_sol_auto(f,sol,t1,y0,n):
  T = [t1*k*1./n for k in range(n+1)]
  Y1 = [sol(t) for t in T]
  Y2 = euler(f,t1,y0,n)
  plt.plot(T,Y1,label='analytique')
  plt.plot(T,Y2,label='numerique')
  plt.legend()
  plt.show()

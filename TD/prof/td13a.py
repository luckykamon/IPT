def primitive1(f,t0,t,yo,n):
  h = (t-t0) * 1. / n
  s = 0
  for k in range(n):
    s += f(t0 + k * h)
  return y0 + h * s

def primitive2(f,t0,tmax,y0,n):#avec append
  h = (tmax-t0) * 1. / n
  l = [y0]
  for k in range(0,n):
    l.append(l[-1] + h*f(t0 + k * h))
  return l

def primitive2(f,t0,tmax,y0,n):#sans append
  h = (tmax-t0) * 1. / n
  l = [0]*(n+1)
  l[0] = y0
  for k in range(0,n):
    l[k+1] = l[k] + h*f(t0 + k * h)
  return l

import matplotlib.pyplot as plt
def fonction_et_primitive(f,t0,tmax,y0):
  n = 1000
  X = [t0 + (tmax-t0)*k*1./n for k in range(n+1)]
  Y1 = [f(x) for x in X]
  Y2 = primitive2(f,t0,tmax,y0,n)
  plt.plot(X,Y1)
  plt.plot(X,Y2)
  plt.show()
  
def sol_autonome(f,t,y0,n):
  a = y0
  h = t*1./n
  for k in range(n):
    a += h * f(a)
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








  
  
  
  
  



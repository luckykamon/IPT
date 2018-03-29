def primitive(f,t0,t,y0,n):
  h = ( t - t0 ) * 1. / n
  s = y0
  for k in range(n):
    s += f( t0 + k * h )
  return h * s

def primitive2(f,t0,t,y0,n):#proche de la precedente
  h = ( t - t0 ) * 1. / n
  s = y0
  l = [s]
  for k in range(n):
    s += f( t0 + k * h ) * h
    l.append(s)
  return l

def primitive2(f,t0,t,y0,n):#version append
  h = ( t - t0 ) * 1. / n
  l = [ y0 ]
  for k in range(n):
    l.append( l[-1] + f( t0 + k * h ) * h )
  return l

def primitive2(f,t0,t,y0,n):#version sans append
  h = ( t - t0 ) * 1. / n
  l = [0]*(n+1)
  l[0] = y0
  for k in range(n):
    l[k+1] = l[k] + f( t0 + k * h ) * h
  return l

import matplotlib.pyplot as plt

def comparaison(f,primf,t0,tmax,y0,n):
  h = ( tmax - t0 ) * 1. / n
  T = [t0 + h * k for k in range(n+1)] 
  Y1 = [primf(t) for t in T]
  Y2 = primitive2(f,t0,tmax,y0,n)
  plt.plot(T,Y1,label = 'analytique')
  plt.plot(T,Y2,label = 'numerique')
  plt.legend()
  plt.show()

'''METHODE D'EULER'''

def sol_autonome(f,t,y0,n):
  h = t * 1. / n
  c = y0
  for k in range(n):
    c = c + h * f(c)
  return c

def sol_num(f,t,y0,n):
  h = t * 1. / n
  l = [y0]
  for k in range(n):
    l.append(l[-1] +h * f( l[-1] ) )
  return l

def comparaison2(f,sol,tmax,y0,n):
  #sol solution analytique de y' = f(y)
  h = tmax * 1. / n
  T = [ h * k for k in range(n+1) ]
  Y1 = [ sol(t) for t in T ]
  Y2 = sol_num(f,tmax,y0,n)
  plt.plot(T,Y1,label = 'analytique')
  plt.plot(T,Y2,label = 'numerique')
  plt.legend()
  plt.show()  
  
def sol_num2(f,t0,tmax,y0,n):
  h = (tmax - t0) * 1. / n
  l = [y0]
  for k in range(n):
    l.append(l[-1] +h * f( l[-1] , t0 + k * h ) )
  return l

def comparaison3(f,sol,t0,tmax,y0,n):
  #sol solution analytique de y' = f(y)
  h = (tmax-t0) * 1. / n
  T = [ t0 + h * k for k in range(n+1) ]
  Y1 = [ sol(t) for t in T ]
  Y2 = sol_num2(f,t0,tmax,y0,n)
  plt.plot(T,Y1,label = 'analytique')
  plt.plot(T,Y2,label = 'numerique')
  plt.legend()
  plt.show()  

from math import cos,sin    
def f(z,t): return cos(t) * z

  
  
  
  
  
  
  
  







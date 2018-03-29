def secante(f,x0,x1,eps):
  a,b = x0,x1
  while abs(b-a) > eps:
    a,b = b,(b - f(b)*(b - a) *1./ (f(b) - f(a)) )
  return b

def fausse_position(f,u,v,eps):
  if f(u)*f(v) > 0:
    raise ValueError
  a,b=u,v
  c = b - f(b)*(b - a) *1./ (f(b) - f(a))
  while abs(c-a) > eps and abs(c-b) > eps :
    if f(c) * f(a) >= 0 :
      a = c
    else:  
      b = c
    c = b - f(b)*(b - a) *1./ (f(b) - f(a))
  return c

'''COMPARAISON GRAPHIQUE'''
  
f = lambda x: x*x -2.

def nb_secante(n):
  a,b = 1,2
  compt = 0
  eps = 10**(-n)
  while abs(b-a) > eps:
    a,b = b,(b - f(b)*(b - a) *1./ (f(b) - f(a)) )
    compt += 1
  return compt

def nb_fausse_position(n):
  a,b=1,2
  c = b - f(b)*(b - a) *1./ (f(b) - f(a))
  compt = 1
  eps = 10**(-n)
  while abs(c-a) > eps and abs(c-b) > eps :
    if f(c) * f(a) >= 0 :
      a = c
    else:  
      b = c
    c = b - f(b)*(b - a) *1./ (f(b) - f(a))
    compt+= 1
  return compt

def nb_dichot(n):
  a,b = 1,2
  compt = 0
  eps = 10**(-n)
  while abs(b-a) > eps:
    c = (a+b)/2.
    if (c*c-2)*(a*a-2) >0:
      a = c
    else:
      b = c
    compt += 1
  return compt
  
def nb_newton(n):
  x = 1
  y = x - (x*x-2) / (2.*x)
  compt = 0
  eps = 10**(-n)
  while abs(y-x) > eps:
    x = y
    y = y - (y*y-2) / (2.*y)
    compt += 1
  return compt

def comparaison():
  X = [k for k in range(15)]
  Y1 = [nb_dichot(x) for x in X]
  Y2 = [nb_newton(x) for x in X]
  Y3 = [nb_secante(x) for x in X]
  Y4 = [nb_fausse_position(x) for x in X]

  import matplotlib.pyplot as plt

  plt.plot(X,Y1,label = 'dichotomie')
  plt.plot(X,Y2,label = 'Newton')
  plt.plot(X,Y3,label = 'secante')
  plt.plot(X,Y4,label = 'fausse position')
  plt.legend()
  plt.show()


'''CALCUL D'INTEGRALE'''

def riemann(f,a,b,n):
  s = 0
  pas = (b-a)*1./n
  for k in range(n):
    s += f(a + k * pas)
  return s * pas

def trapeze(f,a,b,n):
  s = 0
  pas = (b-a)*1./n
  for k in range(n):
    s += f(a + k * pas)+f(a + (k+1)*pas)
  return s * pas / 2.

'''COMPARAISON GRAPHIQUE'''

import scipy.integrate as si

def dif_riemann(f,a,b,n):
  return abs( riemann(f,a,b,n) - si.quad(f,a,b)[0] )
def dif_trapeze(f,a,b,n):
  return abs( trapeze(f,a,b,n) - si.quad(f,a,b)[0] )
  
from math import log

def compare(f,a,b):
  X = [k for k in range(6)]
  Y1 = [log(dif_riemann(f,a,b,10**n) ) for n in X]
  Y2 = [log(dif_trapeze(f,a,b,10**n) ) for n in X]
  plt.plot(X,Y1,label = 'Riemann')
  plt.plot(X,Y2,label = 'trapezes')
  plt.legend()
  plt.show()








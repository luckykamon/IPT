'''PRELIMINAIRES'''

def secante(f,a,b,eps):
  u,v = a,b
  while abs(u-v) > eps:
    u,v = v, ( v-f(v)*(v-u)*1./( f(v)-f(u) ) )
  return v

def fausse_position(f,a,b,eps):
  if f(a) * f(b) > 0:
    raise ValueError
  u,v = a,b
  w = u - f(u)*(v-u)*1./( f(v)-f(u) )
  while abs(w-u) > eps and abs(w-v)>eps:
    if f(w) * f(u) >= 0:
      u = w
    else:
      v = w
    w = u - f(u)*(v-u)*1./( f(v)-f(u) )
    print w
  return w

f = lambda x:x*x-2.
fprim = lambda x:2.*x

'''pour compter'''

def secante2(f,a,b,n):
  eps = 10**(-n)
  compt = 0
  u,v = a,b
  while abs(u-v) > eps:
    u,v = v, ( v-f(v)*(v-u)*1./( f(v)-f(u) ) )
    compt += 1
  return compt

Ysecante = [secante2(f,1,2,n) for n in range(15)]

def fausse_position2(f,a,b,n):
  eps = 10**(-n)
  compt = 0
  if f(a) * f(b) > 0:
    raise ValueError
  u,v = a,b
  w = u - f(u)*(v-u)*1./( f(v)-f(u) )
  while abs(w-u) > eps and abs(w-v)>eps:
    if f(w) * f(u) >= 0:
      u = w
    else:
      v = w
    w = u - f(u)*(v-u)*1./( f(v)-f(u) )
    compt += 1
  return compt

Yfp = [fausse_position2(f,1,2,n) for n in range(15)]

def dichot2(n):
  a = 1
  b = 2
  eps = 10 ** (-n)
  compte = 0
  while b-a > eps:
    c = (a + b) / 2.
    if c*c > 2:
      b = c
    else:
      a = c
    compte += 1
  return compte

Ydichot = [dichot2(n) for n in range(15)]

def newton2(n):
  eps = 10 ** (-n)
  a = 1
  b = a - (a*a-2.)  / (2.*a)
  compte = 0
  while abs(b-a) > eps:
    a,b = b,b - (b*b-2.) / (2.*b)
    compte += 1
  return compte

Ynewton = [newton2(n) for n in range(15)] 

X = range(15)
import matplotlib.pyplot as plt
def graph_compar():
  plt.plot(X,Ydichot,label='dichotomie')
  plt.plot(X,Ynewton,label='Newton')
  plt.plot(X,Ysecante,label='secante')
  plt.plot(X,Yfp,label='fausse position')
  plt.legend()
  plt.show()

'''INTEGRATION'''

def riemann(f,a,b,n):
  pas = (b-a)*1./n
  s = 0
  for k in range(n):
    s += f(a + k * pas)
  return s * pas

def trapeze(f,a,b,n):
  pas = (b-a)*1./n
  s = 0
  for k in range(n):
    s += f(a + k * pas) + f(a + (k+1) * pas)
  return s * pas*1./2
import scipy.integrate as si
from math import log

def graph(f,a,b,n):
  X = [k for k in range(n)]
  Yriem = [log( abs(riemann(f,a,b,10**k)-si.quad(f,a,b)[0] )) for k in range(n)]
  Ytrap = [log( abs(trapeze(f,a,b,10**k)-si.quad(f,a,b)[0] )) for k in range(n)]
  plt.plot(X,Yriem,label = 'Riemann')
  plt.plot(X,Ytrap,label = 'trapezes')
  print 'toto'
  plt.legend()
  plt.show()










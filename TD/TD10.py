def secante(f,a,b,eps):
  u,v = a,b
  while abs(u-v) > eps:
    u,v = v, ( v-f(v)*(v-u)*1./( f(v)-f(u) ) )
  return a

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
#plt.plot(X,Ydichot,label='dichotomie')
plt.plot(X,Ynewton,label='Newton')
plt.plot(X,Ysecante,label='secante')
plt.plot(X,Yfp,label='fausse position')
plt.legend()

import math
import scipy.integrate as si
g = lambda x:x*x-2

def riemann(f,a,b,n):
  r=0
  for k in range(n):
    c=a+k*(b-a)*1./n
    r=r+f(c)
  return ((b-a)*1./n)*r

def erreur1(f,a,b,n):
  return riemann(f,a,b,n)-si.quad(f,a,b)[0]

def trapeze(f,a,b,n):
  s=0
  for j in range(n):
    c=a+j*(b-a)*1./n
    s=s+f(c)*1./2
    c=a+(j+1)*(b-a)*1./n
    s=s+f(c)*1./2
  return ((b-a)*1./n)*s

def erreur2(f,a,b,n):
  return trapeze(f,a,b,n)-si.quad(f,a,b)[0]

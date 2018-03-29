import math
g = lambda y : y*y-2
gprim = lambda y : 2*y

def dichot(f,u,v,eps):
  if f(u)*f(v)>0:
    return 'pas de racines'
  while v-u>eps:
    if f((u+v)/2.)*f(v)==0:
      return (u+v)/.2
    if f((u+v)/2.)*f(v)<0:
      u=(u+v)/2.
    else:
      v=(u+v)/2.
  return u,v

def newton(f,fprim,x0,n):
  x=x0
  for k in range(n):
    x=x-(f(x)*1./fprim(x))
  return x

def newtonbis(f,fprim,x0,eps):
  x=x0-(f(x0)*1./fprim(x0))
  while x0-x>eps:
    x0=x
    x=x-(f(x)*1./fprim(x))
  return x,x0


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
plt.plot(X,Ydichot)
plt.plot(X,Ynewton)
plt.show()




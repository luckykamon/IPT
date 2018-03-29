def dichot(f,u,v,eps):
  if f(u) * f(v) > 0:
    raise ValueError
  a,b = u,v
  while abs(b-a) > eps:
    c = (a + b) / 2.
    if f(c) * f(a) >= 0:
      a = c
    else:
      b = c
  return a

def newton(f,fprim,x0,n):
  a = x0
  for i in range(n):
    a = a - f(a) * 1. / fprim(a)
  return a

def newtonbis(f,fprim,x0,eps):
  a = x0
  b = a - f(a) * 1. / fprim(a)
  while abs(b-a) > eps:
    a,b = b,b - f(b) * 1. / fprim(b)
  return b

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




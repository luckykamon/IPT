def dichot(f,u,v,eps):
  if f(u)*f(v) > 0:
    raise ValueError
  a,b=u,v
  while abs(b-a) > eps :
    c = (a+b) / 2.
    if f(c) * f(a) >= 0 :
      a = c
    else:  
      b = c
  return a

def newton(f,fprim,x0,n):
  x = x0
  for i in range(n):
    x = x - f(x) * 1. / fprim(x)
  return x

def newtonbis(f,fprim,x0,eps):
  x = x0
  y = x - f(x) * 1. / fprim(x)
  while abs(y-x) > eps:
    x = y
    y = y - f(y) * 1. / fprim(y)
  return y

import matplotlib.pyplot as plt


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

X = [k for k in range(15)]
Y1 = [nb_dichot(x) for x in X]
Y2 = [nb_newton(x) for x in X]

plt.plot(X,Y1,label = 'dichotomie')
plt.plot(X,Y2,label = 'Newton')
plt.legend()
plt.show()





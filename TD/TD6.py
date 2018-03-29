import numpy as np
import matplotlib.pyplot as plt

X=np.array([1,3,5,7])
print(type(X))
print(X)

Y=np.arange(-np.pi,np.pi,0.1)
print(type(Y))
print(Y)

Z=np.linspace(0,5,10)
print(type(Z))
print(np.size(Z))

T=np.zeros(7)
print(T)

X=np.linspace(-2,2,10)
Y=np.zeros(10)
for k in range(10):
  Y[k]=(X[k])**2
print(Y)

X = np.arange(-np.pi,np.pi,0.1)
Y = np.sin(X)
print(Y)

X = np.arange(1,10,1)
print(X)
def fact(n):
  p = 1
  for k in range(1,n):
    p = p*k
  return(p)
vfact = np.vectorize(fact)
Y = vfact(X)
print(Y)

l=[2,3,0]
m=np.array(l)
n=vfact(m)

X = np.linspace(-2,2,10)
Y = X**2
plt.axis("equal")
plt.plot(X,Y)
plt.show()

T = np.linspace(0,10,100)
X = T*np.cos(T)
Y = T*np.sin(T)
plt.axis("equal")
plt.plot(X,Y)
plt.show()

T = np.linspace(0,10,100)
Y = np.sin(T)
plt.axis("equal")
plt.plot(T,Y)
plt.show()

T = [k*0.3 for k in range(100)]
X = [0.01*t*np.cos(t) for t in T]
Y = [0.01*t*np.sin(t) for t in T]
plt.axis("equal")
plt.plot(X,Y)
plt.show()

T = np.linspace(-10,10,10000)
Y=np.arctan(T**2+5*T)
plt.axis([0,10,-5,30])
plt.axis("equal")
plt.plot(T,Y,color="red",linewidth=3,linestyle="--")
plt.title("Marmite")
plt.show()

T = np.linspace(-10,10,10000)
Y=np.arcsin(T**2+5*T)
Z=np.sin(T**2+5*T)
W=T
plt.plot(T,Y,color="red",label='arcsin')
plt.plot(T,Z,color="green",label='sin')
plt.plot(T,W,color="brown",label='y=x')
plt.axis("equal")
plt.title("Marmite")
plt.show()

import math

X = [k*0.01 for k in range(157)]
Y = [math.sin(x) for x in X]
plt.plot(X,Y,color='blue', label = 'sin')
plt.plot(Y,X,color='red', label = 'arcsin')
plt.plot(X,X,color='green', linestyle = ':', label = 'y=x')
plt.axis("equal")
plt.legend()
plt.show()


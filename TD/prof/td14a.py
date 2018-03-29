from math import sin
def evol(x,y,h,g,m,l,c):
  return x+h*y , y + h * (-g*1./l*sin(x) - c*1./m * y)

#liste modifiee
def sol_num(pos0,vit0,t,n,g,m,l,c):
  h = t * 1./n
  x = [pos0] + [0] * n
  y = [vit0] + [0] * n
  for k in range(n):
    a = evol(x[k],y[k],h,g,m,l,c)
    x[k+1] = a[0]
    y[k+1] = a[1]
  return x,y

#liste avec append
def sol_num2(pos0,vit0,t,n,g,m,l,c):
  h = t * 1./n
  x = [pos0]
  y = [vit0]
  for k in range(n):
    a = evol(x[-1],y[-1],h,g,m,l,c)
    x.append(a[0])
    y.append(a[1])
  return x,y

#avec append, renvoie liste de couples
def sol_num3(pos0,vit0,t,n,g,m,l,c):
  h = t * 1./n
  u = [(pos0,vit0)]
  for k in range(n):
    u.append(evol(u[-1][0],u[-1][1],h,g,m,l,c))
  return u

#avec numpy
import numpy as np
def evol_np(u,h,g,m,l,c):
  return u + h*np.array([u[1] , (-g*1./l*sin(u[0]) - c*1./m * u[1])])
    
def sol_num4(pos0,vit0,t,n,g,m,l,c):
  h = t * 1./n
  u = np.zeros(n+1)
  u[0] = np.array([pos0,vit0])
  for k in range(n):
    u[k+1] = evol_np(u[k],h,g,m,l,c)
  return x,y  
  np.zeros(7)



import matplotlib.pyplot as plt

def pendule_TX(pos0,vit0,t,n,g,m,l,c):
  sol = sol_num(pos0,vit0,t,n,g,m,l,c)
  T = [k*t*1./n for k in range(n+1)]
  X = sol[0]
  plt.plot(T,X)
  plt.show()
  
def pendule_XY(pos0,vit0,t,n,g,m,l,c):
  sol = sol_num(pos0,vit0,t,n,g,m,l,c)
  X = sol[0]
  Y = sol[1]
  plt.plot(X,Y)
  plt.show()
  
def espace_phases(posmin,posmax,p,vit0,t,n,g,m,l,c):
  for k in range(p):
    pos = posmin + k * (posmax-posmin) * 1./p
    sol = sol_num(pos,vit0,t,n,g,m,l,c)
    plt.plot(sol[0],sol[1])
  plt.show()
    
    
    
    


    

import numpy as np
import matplotlib.pyplot as plt

X = np.array([1,3,5,7])
Y = np.arange(-np.pi,np.pi,0.1)
Z = np.linspace(0,5,10)
Y2 = [-np.pi+0.1*k for k in range(0,int(2*np.pi/0.1)+1)]
Z2 = [0+5./9.*k for k in range(10)]

X = np.linspace(-2,2,10)
Y = X**2

'''
T = np.linspace(0,10,100)
X = np.cos(T)
Y = np.sin(T)
plt.axis("equal")
plt.plot(X,Y)
plt.show()
'''

'''
T2 = [k*10./99 for k in range(100)]
X2 = [t*np.cos(t) for t in T2]
Y2 = [t*np.sin(t) for t in T2]
plt.axis("equal")
plt.plot(X2,Y2)
plt.show()

X1 = np.linspace(-10,10,200)
Y1 = np.arctan(X*X+5*X1)

X = [-10+k*0.1 for k in range(200)]
Y = [np.arctan(x*x+5*x) for x in X]
plt.plot(X,Y,linestyle=':')
plt.show()
'''
X = [-np.pi/2 +np.pi*k/100 for k in range(100)]
Y = [np.sin(x) for x in X]
plt.plot(X,Y,label='sin')
plt.plot(Y,X,label='arcsin')
plt.plot(X,X,linestyle=':',label='y=x')
plt.legend()
plt.axis("equal")
plt.show()




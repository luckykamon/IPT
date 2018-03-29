import numpy as np
import matplotlib.pyplot as plt

'''
T = [k*0.3 for k in range(100)]
X = [0.01*t*np.cos(t) for t in T]
Y = [0.01*t*np.sin(t) for t in T]
plt.axis("equal")
plt.plot(X,Y)
plt.show()
'''
'''
from math import atan
X = [-10+k/10. for k in range(200)]
Y = [atan(x**2+5*x) for x in X]
plt.plot(X,Y,color='green',linestyle=':')
plt.axis([-6.5,1.5,-1.5,2])
plt.show()
'''

import math

X = [k*0.01 for k in range(157)]
Y = [math.sin(x) for x in X]
plt.plot(X,Y,color='blue', label = 'sin')
plt.plot(Y,X,color='red', label = 'arcsin')
plt.plot(X,X,color='green', linestyle = ':', label = 'y=x')
plt.axis("equal")
plt.legend()
plt.show()







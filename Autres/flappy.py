import numpy as np
import matplotlib.pyplot as plt

dt = 0.01  

theta = np.linspace(0, 2*np.pi, 60)

x = np.cos(theta)
y = np.sin(theta)
t=0
x=2
y=2


for i in range(20):
    x = np.Array(
    y = 2+dt
    plt.pause(0.01) # pause avec duree en secondes
    t = t + dt
    plt.plot(x, y)

plt.show()



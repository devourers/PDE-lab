import numpy as np
from math import pi,sin
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm


plt.ion()
fig = plt.figure()
ax = fig.gca(projection='3d')


Lx = 0.15
Ly = 0.15


n = 30

T1 = 0
T2 = 0
T3 = 0
T4 = 0

dx = Lx/n
dy = Ly/n

gamma =  3.4 * (10**(-5))

t_total = 120

dt = 0.1


x = np.linspace(dx/2, Lx - dx/2, n)
y = np.linspace(dy/2, Ly - dy/2, n)

X,Y = np.meshgrid(x,y)


Tx = np.array([60*sin(pi*i/Lx) for i in x])
Ty = np.array([60*sin(pi*i/Ly) for i in y])

TX, TY = np.meshgrid(Tx,Ty)


dTxdt = np.empty(n)
dTydt = np.empty(n)


t = np.arange(0,t_total,dt)

for j in range(1,len(t)):

    ax.clear()

    for i in range(1,n-1):


        dTxdt[i] = gamma*((Tx[i+1]-(2*Tx[i])+Tx[i-1])/dx**2)
        dTydt[i] = gamma*((Ty[i+1]-(2*Ty[i])+Ty[i-1])/dy**2)


    dTxdt[0] = gamma*((Tx[1]-(2*Tx[0])+T1)/dx**2)
    dTydt[0] = gamma*((Ty[1]-(2*Ty[0])+T3)/dy**2)
    dTxdt[n-1] = gamma*((T2-(2*Tx[n-1])+Tx[n-2])/dx**2)
    dTydt[n-1] = gamma*((T4-(2*Ty[n-1])+Ty[n-2])/dy**2)


    Tx = Tx + dTxdt*dt
    Ty = Ty + dTydt*dt
    TX, TY = np.meshgrid(Tx,Ty)

    Z = (TX + TY)

    surf = ax.plot_surface(X,Y,Z, cmap=cm.rainbow,
                           linewidth=0, antialiased = False)

    ax.set_zlim(0,120)
    plt.show()
    plt.pause(0.000000000001)

import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

ro=1.225
m=8.03506
g=9.8
cd=0.295
a=4.5**2*math.pi

def iniciais(v,teta):
    return [0,1.6,math.cos(teta)*v, math.sin(teta)*v]

def derivadas (condicoes,t):
    x=condicoes[0]
    y=condicoes[1]
    vx=condicoes[2]
    vy=condicoes[3]
    dx=vx

    if y > 0:
        dy=vy

    else:
        dy=0

    dvx=-1/2*ro*cd*a*vx/(vx**2+vy**2)**(1/2)/m
    dvy=1/2*ro*cd*a*vy/(vx**2+vy**2)**(1/2)/m-g
    return [dx,dy,dvx,dvy]

listaT = np.arange(0,1,0.001)
angulo=np.arange(0,math.pi/2,0.05)
v0=100
solucoes=[]

for a in angulo:
    ci = iniciais(v0,a)
    solucoes.append(odeint(derivadas,ci,listaT))

for s in solucoes:
    plt.plot(s[:,0],s[:,1])
plt.grid(True)
plt.show()

for s in solucoes:
    plt.plot(listaT,s[:,2])
plt.grid(True)
plt.show()

for s in solucoes:
    plt.plot(listaT,s[:,3])
plt.grid(True)
plt.show()
altura30=[]

for s in solucoes:
    c=0
    while c<len(s[:,1]) and s[:,1][c] < 15:
        c+=1
    if c<len(s[:,0]):
        altura30.append(s[:,0][c])

angulos=[]

for a in angulo:
    angulos.append(a)

while len(angulos)>len(altura30):
    del angulos[len(altura30)]
plt.plot(angulos,altura30)
plt.grid(True)
plt.show()

validacao_x = [1.1091316298483154,
10.180698360989513,
20.05700906036852,
30.033085615392437,
40.00738063727986,
50.08042349587702,
60.05140995622519,
70.02061488343683,
80.08856764735823,
90.05395500356306,
100.01806983609893]

validacao_y = [0.10101010101010122
,0.30303030303030365
,0.20202020202020243
,-0.10101010101010122
,-0.7575757575757578
,-1.8181818181818183
,-3.1313131313131315
,-4.797979797979798
,-6.86868686868687
,-9.292929292929294
,-11.969696969696969]

plt.plot(validacao_x, validacao_y, 'ro')
plt.grid(True)
plt.show()

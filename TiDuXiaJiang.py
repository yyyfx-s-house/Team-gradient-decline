from math import sin,cos, pi
from random import*
from time import*

start_time = time()
def cy(x):
    return (2*x + 5*pi*sin(pi*x))
def ly(x):
    return (x**2+5*cos(pi*x))
pos=5
v=0.001
while 1:
    nps=pos-cy(pos)*v
    if abs(nps - ip)<0.0001:
        print(time()-start_time,nps)
        break
    else:
        pos = nps

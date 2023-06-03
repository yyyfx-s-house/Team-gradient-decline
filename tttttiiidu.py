from math import sin,cos, pi
from random import*
from time import*

start_time = time()
def cy(x):
    return (2*x + 5*pi*sin(pi*x))
def ly(x):
    return (x**2+5*cos(pi*x))
b=0
pos=[[randint(4,6),uniform(0.001, 0.01)] for i in range(6)]
while 1:
    i=0
    while 1:
        ip = pos[i][0]
        v=pos[i][1]
        nps=ip-cy(ip)*v
        
        print(pos,i)
        if ly(ip) > ly(min(pos, key=lambda x: ly(x[0]))[0]):
            if abs(nps - ip)<0.0001:
                nps *= i+1
            pos[i][1] *= 1 - (2-i)
            pos[i][1]+= pos[i][1]-(min(pos, key=lambda x: ly(x[0]))[1])/5
            pos[i][0]= nps+(pos[i][0]-(min(pos, key=lambda x: ly(x[0]))[0])/5)
            
        else:
            if abs(nps - ip)<0.0001:
                print(time()-start_time,ip)
                b=1
        pos[i][0] *= 1-(6-i)**2
        if i == len(pos)-1:
            break
        for i in range(len(pos)):
            pos[i][0] = round(pos[i][0],100)
            pos[i][1] =	round(pos[i][1],100)
    if b==1:
        break
            

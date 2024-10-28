import numpy as np
import random as rd

def f(x):
    return np.cos(x)-x

def fDer(x):
    return -np.sin(x)-1

iterasjonSum = 0
loopAmount = 1000

for i in range(loopAmount):
    tall = rd.random()*1000 - 500
    iterasjon = 0
    while abs(f(tall))>10**-16:
        tall = tall -(f(tall)/fDer(tall))
        iterasjon+=1
    if abs(tall)!=np.inf:
        iterasjonSum+=iterasjon
        print(f"{tall}  :   {iterasjon}") 

print(iterasjonSum/loopAmount)


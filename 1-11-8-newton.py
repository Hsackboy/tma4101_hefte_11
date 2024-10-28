import numpy as np
import random as rd

def f(x):
    return 2*np.sin(2*x)+np.pi -4 *x

def fDer(x):
    return 4*np.cos(2*x) -4

maxIterasjons = 10_000

for i in range(100):
    tall = rd.random()*100 -50
    iterasjon = 0
    while abs(tall-f(tall))>10**-16:
        tall = f(tall)
        iterasjon+=1
        if (iterasjon>maxIterasjons):
            break
    print(f"{i:<3}:{tall}  :   {iterasjon}") 
    # print(f"{i:<3}:{np.cos(tall)}  :   {iterasjon}") 


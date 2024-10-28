import numpy as np
import random as rd

def f(x):
    return np.log(x)*x -1

def fDer(x):
    return np.log(x)+1  

maxIterasjons = 10_000

for i in range(-50,50):
    tall = i
    iterasjon = 0
    print(f"{i:<3}",end=":")
    while (abs(f(tall))>10**-16):
        tall = tall -(f(tall)/fDer(tall))
        iterasjon+=1
        if (iterasjon>maxIterasjons):
            break

    print(f"{tall}  :   {iterasjon}") 


import numpy as np
import random as rd

def f(x):
    return (2*np.sin(2*x)+np.pi)/4

maxIterasjons = 10_000

for i in range(-50,50):
    tall = i
    iterasjon = 0
    while abs(tall-f(tall))>10**-16:
        tall = f(tall)
        iterasjon+=1
        if (iterasjon>maxIterasjons):
            break
    print(f"{i:<3}:{np.cos(tall)}  :   {iterasjon}") 
    print(f"{i:<3}:{tall}  :   {iterasjon}") 


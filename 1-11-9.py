import numpy as np
import random as rd

def f(x):
    return -(x**3 +x**2+1)

def g(x):
    return x**3 +x**2 + x +1

maxIterasjons = 10_000

for i in range(1):
    tall = 0.3 + 0.1 * 1j
    iterasjon = 0
    while abs(tall-f(tall))>10**-16:
        tall = f(tall)
        iterasjon+=1
        if (iterasjon>maxIterasjons):
            break 
    print(f"{i:<3}:{tall}  :   {iterasjon}") 
    print(g(tall))

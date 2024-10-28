import numpy as np
import random as rd

def f(x):
    return np.exp(1/x)

iterasjonSum = 0
loopAmount = 1000

for i in range(loopAmount):
    tall = rd.random()*1000 - 500
    iterasjon = 0
    while abs(tall-f(tall))>10**-16:
        tall = f(tall)
        iterasjon+=1
    if abs(tall)!=np.inf:
        iterasjonSum+=iterasjon
        print(f"{tall}  :   {iterasjon}") 

print(iterasjonSum/loopAmount)
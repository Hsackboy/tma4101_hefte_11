import numpy as np
import random as rd


iterasjonSum = 0
loopAmount = 1000

for i in range(loopAmount):
    tall = rd.random()*1000 - 500
    iterasjon = 0
    while tall!=0.7390851332151607:
        tall = np.cos(tall)
        iterasjon+=1
    if abs(tall)!=np.inf:
        iterasjonSum+=iterasjon
        print(f"{tall}  :   {iterasjon}") 

print(iterasjonSum/loopAmount)
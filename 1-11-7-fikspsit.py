import numpy as np
import random as rd

def f(x):
    if x == 0:
        return 0
    return np.exp(1/x)



for i in range(-50,50):
    tall = i
    iterasjon = 0
    while abs(tall-f(tall))>10**-16:
        tall = f(tall)
        iterasjon+=1
    print(f"{i:<3}:{tall}  :   {iterasjon}") 


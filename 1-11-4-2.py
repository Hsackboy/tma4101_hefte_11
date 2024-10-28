import numpy as np
import random as rd

def f(x):
    return 1/(np.log(x))


for i in range(10):
    tall = rd.random()*1000 - 500
    iterasjon = 0
    while abs(tall-f(tall))>10**-16:
        tall = f(tall)
        iterasjon+=1
    print(f"{tall}  :   {iterasjon}")



import numpy as np
import random as rd

def f(x):
    return np.cos(x)-x

def fDer(x):
    return -np.sin(x)-1



for i in range(-50,50):
    tall = i
    iterasjon = 0
    while abs(f(tall))>10**-16:
        tall = tall -(f(tall)/fDer(tall))
        iterasjon+=1
    print(f"{i:<3}:{tall}  :   {iterasjon}") 


import numpy as np
import random as rd

for i in range(10):
    tall = rd.random()*100
    for _ in range(100):
        tall = np.cos(tall)
    print(tall)
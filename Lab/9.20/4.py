import random 
import math 
S = 1*21
N = 100000
C = 0 
for i in range(N): 
    x = random.uniform(2.0,3.0) 
    y = random.uniform(0.0,21.0)
    if y <= math.sin(x)*4*x + math.pow(x,2): 
        C += 1 
I = C / N * S 
print(I)
def trailingZeroes(n):
    import numpy as np
    if n == 0: return 0
    fact = str(np.math.factorial(n))[::-1]
    count = 0 
    for i in fact:
        if int(i) == 0:
            count+=1
        if int(i) > 0:
            return count

print(trailingZeroes(5))
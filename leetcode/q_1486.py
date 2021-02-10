def xorOperation(n, start):
    return_var=0
    for xor in range(n): return_var ^= (start + 2*xor)
    return return_var
    

print(xorOperation(5,0))

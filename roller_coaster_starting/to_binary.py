n=75.0
def to_binary(n):
    x=n
    k=[]
    while (n>0):
        q=int(float(n%2))
        k.append(q)
        n=(n-q)/2
            
    string= k[::-1]
    return "".join([str(i) for i in string])

print(to_binary(n))

def to_base_2(n):
    max_num = n

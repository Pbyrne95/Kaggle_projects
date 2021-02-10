n=600
def to_binary(n):
    x=n
    k=[]
    while (n>0):
        q=int(float(n%2))
       
        k.append(q)
        n=(n-q)/2
            
    string= k[::-1]
    return  "".join([str(i) for i in string])

def to_binary_count(n):
    factors = 1
    record=[factors]
    while (factors < n):
        factors *= 2
        record.append(factors)
    if record[-1] > n: record.remove(record[-1])
    binary_str = ''
    current_sum = n
    for i in reversed(record):
        if (current_sum>=i):
            current_sum-=i
            binary_str+='1'
        elif (current_sum<i):
            binary_str+='0'
            continue
    return binary_str
print(to_binary_count(n))

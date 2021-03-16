n=600

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

def binary_count(binary):
    double = 1
    double_list = [double]
    binary_to_num=0
    while len(double_list) < len(binary):
        double = double * 2
        double_list.append(double)

    double_list = double_list[::-1]
    for i in range(len(binary)):
        if binary[i] == '1':
            binary_to_num+=double_list[i]   
    
    return binary_to_num
     
def to_binary(n):
    n =  int(n)
    x=n
    k=[]
    while (n>0):
        q=int(float(n%2))
       
        k.append(q)
        n=(n-q)/2
            
    string= k[::-1]
    return  "".join([str(i) for i in string])
def works(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal



p1=0
placeHoler = ''
while p1 < 13:
    placeHoler +='1'
    p1+=1


print(to_binary(10))



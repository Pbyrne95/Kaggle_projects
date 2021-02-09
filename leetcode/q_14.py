def longestCommonPrefix1(strs):
    answer = ''
    if len(strs) ==0: 
        return answer

    short = sorted(strs, key=len)[0] # shortest string
    count = 0
    for i in range(len(short)):
        for j in range(len(strs)): 
            if strs[j][i] == short[i]: #iterates through the nth letter of each string, adds it if the count reaches len(strs)
                count+=1
            if count == len(strs): 
                answer += short[i]
            if strs[j][i]!= short[i]:  #stops the loop when it finds a letter that doesn't match
                return answer
        count = 0
            

#     return answer
        
def longestCommonPrefix(strs):
    short = sorted(strs, key=len)
    checl_leng = len(short[0])
    if strs[0][-1] == strs[-1][-1]:
        same_length = [i[:checl_leng-1] for i in short]
    else:
        same_length = [i[:checl_leng] for i in short]
    
    count_dict = dict()
    for i in same_length:
        for j in i:
            if j not in count_dict:
                count_dict[j] =1
            else:
                count_dict[j] +=1
    
    res = {k:v for (k,v) in count_dict.items()}
    return "".join(res.keys())


strs = ["cir","car"]




def plusOne(digits):return sorted(list(set(digits)))


            
     




head = [1,1,2,3,3]
print(longestCommonPrefix(strs))
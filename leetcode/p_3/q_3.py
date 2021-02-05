substring = "abcabcbb"
substring1 = "pwwkew"
def to_leng(x):
    return [(x[k+1]-x[k])>=0 for k in range(len(x)-1)]

def to_leng1(x):
    p1 = 0
    p2 = 1
    list_of_true = []
    while p1 < len(x):
        if p2 < len(x):
            temp = (x[p1]+1 == x[p2])
            if temp:
                list_of_true.append(temp)
        elif p2 == len(x):
            temp = (x[p1-1]+1 == x[-1])
            if temp:
                list_of_true.append(temp)
        p1+=1
        p2+=1
    return list_of_true

def all_ints(x):
    all_nums = []
    for i in x:
        for nums in i:
            all_nums.append(int(nums))
    return all_nums

def lengthOfLongestSubstring(s):
    record = []
    recorded_substring = []
    seen = []
    return_sub = ''
    p1 = 0
    all_indexs = ''
    while p1 < len(s)-1:
        if s[p1] != s[p1+1] and s[p1] and s[p1] not in seen:
            return_sub +=  s[p1]
            all_indexs += str(p1)
            seen.append(s[p1])
            record.append([all_indexs])
        
            
        p1+=1
    
    return record

def all_together(param):
    iter = lengthOfLongestSubstring(param)
    all_nums = [all_ints(i) for i in iter]
    return max([len(to_leng1(i)) for i in all_nums])
    

x = [0,2,3,4]
print(all_together(substring1))


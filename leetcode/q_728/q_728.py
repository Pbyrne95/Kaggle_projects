left = 1
right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

def selfDividingNumbers(left,right):
    def helper(all_nums):
        if '0' in str(all_nums): return False
        else:
            for i in str(all_nums):
                boolen = True
                for nums in i:
                    if all_nums % int(nums) != 0:
                        boolen = False
                        return boolen
        return boolen
    
    return [i for i in range(left,right+1) if helper(i)]
        

print(selfDividingNumbers(left,right))




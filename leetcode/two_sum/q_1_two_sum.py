


List1 = [3,2,4]
target = 6
# Solution 1 
def twoSum1(nums,target):
    # iterate through the to find 
    list_of_values = []
    for ind1,i in enumerate(nums):
        for ind2,j in enumerate(nums):
            if i+j==target:
                list_of_values.append(i)
    return list_of_values

def first_points(target_list,target):
    index_list = twoSum1(target_list,target)
    list_comp = [(i,v) for i,v in enumerate(target_list) if v in index_list]

    p1,p2,max_am =0,1,len(list_comp)-1
    final_list = ''
    while p2 <= max_am:
        if list_comp[p1][1] + list_comp[p2][1] == target:
            final_list = str(list_comp[p1][1]) + ',' +  str(list_comp[p2][1])
            break
        p1+=1
        p2+=1
    return [int(final_list[0]),int(final_list[-1])]  
                   
        


# solution 2 

def twoSum(nums,target):
    iter_dict = dict()
    
    for i in range(len(nums)):
        num = nums[i]
        current = target - num
        if num in iter_dict:
            return [iter_dict[num], i]
        else:
            iter_dict[current] = i 
    
   


# Two Sum || 
List = [1,3,4,5,7,10,11]
def twoSum(numbers, target):
    p1,p2 = 0,len(numbers)-1
    starting_point = numbers[p1]
    end_point = numbers[p2]
   
    while p1 < p2:
        temp = starting_point + end_point
        if temp > target:
            p2-=1
        if temp < target:
            p1+=1
        elif temp == target:
            return [p1 +1,p2 +1]
    

def final_solution(numbers,target):
    p1,p2 = 0,len(numbers)-1

    while p1 < p2:
        cur_sum = numbers[p1] + numbers[p2]

        if cur_sum > target:
            p2 -=1
        elif cur_sum < target:
            p1+=1
        else:
            return [p1 +1, p2 +1]
print(final_solution(List,9))

# iter_dict = dict()
        
# for i in range(len(nums)):
#     num = nums[i]
#     current = target - num
#     if num in iter_dict:
#         return [iter_dict[num],i]
#     else:
#         iter_dict[current] = i

## Solution one 
def maxProductPath(grid):
    from numpy import prod

    if sum(grid[0]) < 0:
        return -1

    # iterate through each level of the grid 
    nums_less_one = []
    p1 = 0 # this variable will index through each level of the list 
    temp = [] # this list will hold all values matching creteria at level of the grid 

    # loop runs while p1 is less then the length of the grid
    while p1 < len(grid):
        
        # goes through each set of numbers in the grid 

        for num in grid[p1]:
            if num <= 1 and p1 >= 1:
                temp.append(num)
            elif p1 == 0:
                if num == 1:
                    temp.append(num)
                    break
        
        nums_less_one.append([temp])
        temp = []
        p1+=1
    
    # now we have all numbers less then one - find all numbers that match 
    # -- cant go to higher number -> lower -> higher - but can do lower -> higher and lower -> lower ->..
    p1 = 0
    nums_to_product = []
    while p1 < len(nums_less_one):
        for lists in nums_less_one[p1]:
            if len(lists) > 2:
                if lists[0] >= lists[-1]:
                    nums_to_product.append(lists[:len(lists)-1])
            else:
                nums_to_product.append(lists)

        p1+=1
    actual_product = [val for sublist in nums_to_product for val in sublist if val != 0]
    
    return prod(actual_product)




## solution 2 - refactered solution one 

class Solution:
    def maxProductPath1(self, grid):
        n_r = len(grid); n_c = len(grid[0])
        dp_max = [[0]*n_c for _ in range(n_r)]
        dp_min = [[0]*n_c for _ in range(n_r)]
        
        dp_max[0][0] = dp_min[0][0] = grid[0][0]
        
        for r in range(1, n_r):
            dp_max[r][0] = dp_min[r][0] = grid[r][0]*dp_max[r-1][0]
        
        for c in range(1, n_c):
            dp_max[0][c] = dp_min[0][c] = grid[0][c]*dp_max[0][c-1]
            
        for r in range(1, n_r):
            for c in range(1, n_c):
                dp_max[r][c] = max(dp_max[r-1][c]*grid[r][c], dp_max[r][c-1]*grid[r][c], dp_min[r-1][c]*grid[r][c], dp_min[r][c-1]*grid[r][c])
                
                dp_min[r][c] = min(dp_max[r-1][c]*grid[r][c], dp_max[r][c-1]*grid[r][c], dp_min[r-1][c]*grid[r][c], dp_min[r][c-1]*grid[r][c])
                
        if dp_max[n_r-1][n_c-1] < 0: return -1

        return dp_max[n_r-1][n_c-1]%(10**9+7)


grid2 = [[1,4,4,0],[-2,0,0,1],[1,-1,1,1]]
print(maxProductPath(grid2))
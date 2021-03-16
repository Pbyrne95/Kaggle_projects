class Solution:
    def fourSum(self, nums, target):
        nums = sorted(nums)
        output=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                y = j+1
                k = len(nums)-1
                while y < k:
                    temp = (nums[i],nums[j],nums[y],nums[k])
                    if sum(temp) == target and temp not in output:
                        output.add(temp)
                    elif sum(temp) > target:
                        k-=1
                    else:
                        y+=1
        return output


if __name__ == "__main__":
    temp = Solution()    
    y = [1,0,-1,0,-2,2]
    target = 0
    print(temp.fourSum(y,target))


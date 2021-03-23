class Solution:
    def subsetsWithDup(self, nums):
        outputList = [[]]
        for i in range(len(nums)):
         for j in range(len(outputList)):
            temp = [nums[i]]+outputList[j]
            temp.sort()
            if temp not in outputList: outputList.append(temp)

        return outputList

    def sub_one(self, nums):
        numstemp=[inner for outer in nums for inner in outer]
        
        return numstemp

    
if __name__ == "__main__":
    temp = Solution()
 
    print(temp.subsetsWithDup([1,2,2]))
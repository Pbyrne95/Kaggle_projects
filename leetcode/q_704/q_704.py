class Solution:
    def search(self, nums,target):
        for index,value in enumerate(nums):
            if value == target:
                return index
        return (-1)


if __name__ == "__main__":
    temp = Solution()
    print(temp.search([-1,0,3,5,9,12],9))


class Solution:
    def subtractProductAndSum(self, n):
        import numpy as np
        temp = str(n)
        intChar = [int(char) for char in temp]
        product = np.prod(intChar)
        sumof = sum(intChar)
        return product-sumof

if __name__ == "__main__":
    n = 234
    # Productofdigits = 2 * 3 * 4 = 24 
    # Sumofdigits = 2 + 3 + 4 = 9 
    Result = 24 - 9 == 15

    temp = Solution()
    print(temp.subtractProductAndSum(n))

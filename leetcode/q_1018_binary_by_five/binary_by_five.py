class Solution:
    def to_binary(self,num):
        decimal = 0
        for digit in num:
            decimal = decimal*2 + int(digit)

        return decimal % 5 == 0

    def prefixesDivBy5(self, A):
        sublist = []

        for i in range(1,len(A)+1):
            sublist.append(A[0:i])

        outList = [self.to_binary(i) for i in sublist]
        
        return outList



if __name__ == "__main__":
    temp = Solution()
    print(temp.prefixesDivBy5([1,1,1]))
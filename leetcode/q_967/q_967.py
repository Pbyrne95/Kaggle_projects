class Solution:
    def repeatedNTimes(self, A):
        from collections import Counter
        val = Counter(A)
        max_val = {k:v for k,v in val.items() if v > 1 }
        return int(list(max_val.keys())[0])
    

if __name__ == "__main__":
    var = Solution()
    print(var.repeatedNTimes([2,1,2,5,3,2]))
    print(var.repeatedNTimes([5,1,5,2,5,3,5,4]))

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B: return True
        run_time = len(A)
        while (run_time > 0):
            if B != A:
                x = B[0]
                B = B[1::] + x
                run_time-=1
              
            else:
                return True

        return False



if __name__ == "__main__":
    temp = Solution()

    E = "abcde"
    F = "abced"

    A = "abcde"
    B = "cdeab"

    # print(temp.rotateString(E,F))
    print(temp.rotateString(A,B))
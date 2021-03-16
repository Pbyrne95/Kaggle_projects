class Solution:
    def longestWord(self, words):
        words = sorted(words)
        chunk_stack = []
        stack_level = 0

        current_stack=[]

        for i in range(len(words)-1):
            
            if words[i] not in words[i+1] and i != len(words)-1:
                # print(current_stack)
                chunk_stack.append(sorted(current_stack))
                current_stack = []
                           
            else:
                # print(words[i])
                current_stack.append(words[i+1]) 

        # chunk_stack.append(current_stack[-1])
        max_len = max([len(i) for i in chunk_stack])
        chunk_stack = [i for i in chunk_stack if len(i) == max_len]
                  
        return chunk_stack
        

     
        

if __name__ == "__main__":
    temp = Solution()
    # print(temp.longestWord(["w","wo","wor","worl", "world"]))
    y = ["a","banana","app","appl","ap","apply","apple"]
    x = ["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]
    print(temp.longestWord(y))
    
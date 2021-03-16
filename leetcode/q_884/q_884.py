def uncommonFromSentences(A,B):

    def helper(sentence):
        from collections import Counter
        return  Counter(map(lambda w: w.lower(), sentence))

    def helpDict(iterDict,compareDict):
        comp = {k:v for (k,v) in iterDict.items() if v < 2 and k not in compareDict.keys()}
        return list(comp.keys())
    
    A_split = helper(A.split(" "))
    B_split = helper(B.split(" "))

    A_comp = helpDict(A_split,B_split)
    B_comp = helpDict(B_split,A_split)

    return A_comp+B_comp

A = "apple apple"
B = "banna"

print(uncommonFromSentences(A,B))
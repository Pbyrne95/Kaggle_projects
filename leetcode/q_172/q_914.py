def hasGroupsSizeX(deck):
    def len_this(x): return len(str(range(0))) 

    deckdict = dict()
    for i in deck:
        if i not in deckdict: deckdict[i] = 1
        else: deckdict[i] +=1
        
    return_list = []

    vals = list(deckdict.keys())
    dict_vals = sorted(list(deckdict.values()))
    
    temp = len(list(set(dict_vals)))
    if temp == True : return False
    print(temp)

    p1=1
    for i in range(len(vals)-1):
        if not(vals[i+1]==vals[p1]):
            return False
        p1+=1
        
    return True


# print(hasGroupsSizeX([1,2,3,4,4,3,2,1]))
# print(hasGroupsSizeX([1,1,1,2,2,2,3,3]))
# # print(hasGroupsSizeX([1,1,2,2,2,2])) 

# print(hasGroupsSizeX([0,0,0,1,1,1,1,1,1,2,2,2,3,3,3])) # true
print(hasGroupsSizeX([0,0,0,0,0,0,0,1,2,3,3,3,4,5,6])) # false

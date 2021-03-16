class Sorting_algos:

    def bubbleSort(self,L):

        temp = 0 
        max_pos = len(L)-1
        
        for i in range(len(L)-1):
            for j in range(len(L)-1,0,-1):
                if(L[j] < L[j-1]):
                    temp = L[j]
                    L[j] = L[j-1]
                    L[j-1] = temp
        return L



if __name__ == "__main__":
    temp = Sorting_algos()
    x = [23,47,12,39,99,100,43,21,89,1,23]
    print(temp.bubbleSort(x))
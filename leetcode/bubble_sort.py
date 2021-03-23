class Sorting_algos:

    def bubbleSort(self,L):

        #iterator to dictate how long the loop is run for
         
        runTime = len(L)-1

        # for loop which run each elemet in the loop

        for i in range(runTime):
            for j in range(runTime,0,-1):

                if(L[j] < L[j-1]):
                    temp = L[j]
                    L[j] = L[j-1]
                    L[j-1] = temp
                print(L)
        return L


if __name__ == "__main__":
    temp = Sorting_algos()
    x = [23,47,12,39,99,100,43,21,89,1,23]
    print(temp.bubbleSort(x))
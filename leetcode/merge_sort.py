class Merge_sort:

    def get_middle(self,L):
        return len(L)//2

    
    def mergeSort(self,arr):
        # break cluase for recurrsion
        if len(arr) > 1:

            midPoint = self.get_middle(arr)

            firstHalf = arr[:midPoint]
            secondHalf = arr[midPoint:]

            self.mergeSort(firstHalf)
            self.mergeSort(secondHalf)

            i=j=k=0

            while i < len(firstHalf) and j < len(secondHalf):
                if firstHalf[i] < secondHalf[j]:
                    arr[k] = firstHalf[i]
                    i+=1
                else:
                    arr[k] = secondHalf[j]
                    j+=1
                k+=1
            
            while i < len(firstHalf):
                arr[k] = firstHalf[i]
                i+=1
                k+=1
            while j < len(secondHalf):
                arr[k] = secondHalf[j]
                j+=1
                k+=1

            return arr


        

       

if __name__ == "__main__":
    temp = Merge_sort()
    x = [23,47,12,39,99,100,43,21,89,1,23]
    print(temp.mergeSort(x))
    
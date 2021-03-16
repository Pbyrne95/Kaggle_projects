class Merge_sort:

    def get_middle(self,L):
        return len(L)//2

    
    def sortSplit(self,L):
        temp = 0
        maxPos = len(L)-1

        for i in range((len(L)-1)):
            for j in range(len(L)-1,0,-1):
                if(L[j] < L[j-1]):
                    temp = L[j]
                    L[j] = L[j-1]
                    L[j-1] = temp
        return L


    def mergeSort(self,arr):
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        L = self.sortSplit(L)

 
        # Sorting the second half
        R = self.sortSplit(R)

        i = j = k = 0
 
        # # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1


        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
        return arr

        

       

if __name__ == "__main__":
    temp = Merge_sort()
    x = [23,47,12,39,99,100,43,21,89,1,23]
    print(temp.mergeSort(x))
    
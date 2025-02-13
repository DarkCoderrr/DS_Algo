class quicksort:
    
    def partition(list,low,high):
        pivot=list[high] #Let pivot as the last element
        i=low-1          #initialize the pointer for the smaller list, "i" keeps track of the position where elements greater than the pivot should be placed.

        for j in range(low,high):  #The loop runs from index low to high - 1 (excluding the pivot).
            if list[j]<=pivot:  #j is used to iterate through the array, comparing each element with the pivot. If the current element list[j] is greater than the pivot, 
                                #it should be moved to the left partition.
                i+=1
                list[i],list[j]=list[j],list[i] #swaping of element

        list[i+1],list[high]=list[high],list[i+1] #placing pivot on right position for next iteration
        return i+1  #returns partition index
    
    def sorting(list,low,high):
        if low<high:
            prt=quicksort.partition(list,low,high)  #this will call the latest Partition Index

            quicksort.sorting(list,low,prt-1)       # Recursively sort left partition
            quicksort.sorting(list,prt+1,high)      # Recursively sort right partition

       

def main():
    #inputnumber
    n=[2,4,5,1,3,7,6]
    quicksort.sorting(n,0,len(n)-1)
    print(f"The Sorted Array is {n}")

if __name__=="__main__":
    main()  

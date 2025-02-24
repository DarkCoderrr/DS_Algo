class RemoveDuplicates:

    #Approach Using SET
    def remove(list):
        present=set()   #keep track of element already present
        result=[]       #keep track of keeping a list of element in same order
        for x in list:
            if x not in present:
                present.add(x)
                result.append(x)

        return result
    
    #approach using 2 pointer
    def RemoveusingTwoPointer(list):
         
         left=0     #slow pointer for tracking unique element in order
         if not list:
              return []        
  
         for right in range(1,len(list)):
            if list[right]!=list[left]:   #condition to find a unique element
                 left+=1                  #Move Slow Pointer to the Right
            list[left]=list[right]        #update the left pointer with a unique element
         return list[:left+1]             # Return till the last value of left pointer
                 



def main():
    list=[1,1,2,3,4,4,4,4,5,5,6,7,7,8,8,8,8,9]
    print(RemoveDuplicates.remove(list))
    print(RemoveDuplicates.RemoveusingTwoPointer(list))


if __name__=="__main__":
        main()

                
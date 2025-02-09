class factorial:
    
    def calculatefactorial(n):
        #base condition
        if n==0 or n==1:
            return 1
        else:
            #result to log every number's factorial
            result=n * factorial.calculatefactorial(n-1)
            print(f"factorial for number {n} is equal to factorial={result}")
            return result
        

def main():
    #inputnumber
    n=int(input("Enter the number here="))
    result=factorial.calculatefactorial(n)
    print(f"The factorial of {n} is {result}")

if __name__=="__main__":
    main()  

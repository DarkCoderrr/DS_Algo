class fibonaci:
    def calculatefibonaci(n):
        if n<=1:
            return n
        else:
            return fibonaci.calculatefibonaci(n-1) +fibonaci.calculatefibonaci(n-2)
        
def main():
    number=int(input("Enter the Number="))
    result=fibonaci.calculatefibonaci(number)
    print(f"the fibonaci number for {number}th number is {result} ")

if __name__=="__main__":
    main()

    
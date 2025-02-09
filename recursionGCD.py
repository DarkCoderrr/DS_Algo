class gcd:

    def calculategcd(num1,num2):
        if num2==0:
            return num1
        else:
            return gcd.calculategcd(num2,num1%num2)
        

def main():
        number1=24
        number2=42
        result=gcd.calculategcd(number1,number2)
        print(f"The GCD of {number2} and {number1} equals to {result}")
    
if __name__=="__main__":
    main()    
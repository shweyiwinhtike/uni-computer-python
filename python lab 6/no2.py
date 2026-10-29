while True:
    def isPrime(x):
        if x < 2:
            return False
        elif x == 2:
            return True
        
        divider = abs((x/2)+1)
        for i in range(1, divider):
            
            if x % i == 0:
                return False
        return True
        
    inputx = int(input("Enter the value of x: "))
    print(isPrime(inputx))
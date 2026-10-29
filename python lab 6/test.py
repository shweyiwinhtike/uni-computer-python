while True:
    def isPrime(x):
        if x < 2:
            return False
        elif x == 2:
            return True
        
        divisor = 2
        while divisor <= inputx/2:
            if x % divisor == 0:
                return False
            divisor+=1
        return True
  
    inputx = int(input("Enter the value of x: "))
    print(isPrime(inputx))
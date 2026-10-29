class Calculator:
    def __init__(self, acc=0.0) -> None:
        self.acc = acc
    
    def set_accumulator(self, a=0.0):
        self.acc = a

    def get_accumulator(self):
        return float(self.acc)
    
    def add(self, x):
        self.acc += x

    def substract(self, x):
        self.acc -= x

    def multiply(self, x):
        self.acc *= x

    def divide(self, x):
        if x == 0:
            print("Cannot divide by zero!")
        else: self.acc /= x

    def print_result(self):
        print(f"Result: {self.acc}")
    


class Sci_calc(Calculator):
    def __init__(self, acc=0.0) -> None:
        super().__init__(acc)

    def factorial(self):
        if self.acc < 0:
            print("Factorial Cannot be negative")
        elif self.acc == 0:
            print("Factorial cannot be zero")
        elif self.acc != int(self.acc):
            print("Factorial can't be float")
        else:
            temp = self.acc
            factorial = 1
            while temp >= 1:
                factorial *= temp
                temp -= 1
                return factorial

    def print_result(self):
        print(f"Result: {self.acc}")

    def square(self):
        self.acc = self.acc ** 2
    
    def exp(self, x):
        self.acc = self.acc ** x
    
    def factorial(self):
        if self.acc == 0:
            print("Cannot factorial zero")
        elif self.acc < 0:
            print("Cannot factorial negative number")
        else:
            if int(self.acc) == self.acc:
                temp = self.acc
                factorial = 1
                while temp >= 1:
                    factorial *= temp
                    temp -= 1
                self.acc = factorial
            else:
                print("cannot factorial float")
    
    def print_result(self):
        print(f"Result: {self.acc:.2e}")





   
cal = Calculator()
print("Test calculator:")
print("Start value:", cal.get_accumulator())
cal.set_accumulator(5)
print("Check set:", cal.get_accumulator())
cal.add(5)
print("Check Add:")
cal.print_result()
cal.substract(4.5)
print("Check Subtract:")
cal.print_result()
cal.multiply(2)
print("Check multiply:")
cal.print_result()
print("Check divide by zero:")
cal.divide(0) # print "Cannot Divide By Zero." here
cal.print_result() # acc should stay the same
cal.divide(2)
print("Check divide:")
cal.print_result()




print("\nTest sci_cal:")
sc = Sci_calc()
print("Start value:", sc.get_accumulator())
sc.set_accumulator(5)
print("Check set:", sc.get_accumulator())
print("Check square:")
sc.square()
sc.print_result()
print("Check exp:")
sc.exp(-1)
sc.print_result()
print("Check factorial to float:")
sc.factorial() # print "Cannot Factorial Float." here
sc.print_result() # acc should stay the same
sc.set_accumulator(-5)
print("Check factorial to negative:")
sc.factorial() # print "Cannot Factorial Negative." here
sc.print_result() # acc should stay the same
sc.set_accumulator(4)
print("Check factorial:")
sc.factorial()
sc.print_result()
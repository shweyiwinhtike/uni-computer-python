class Calculator:
    def __init__(self, acc=0.0) -> None:
        self._acc = acc

    def set_accumulator(self, a: int):
        if not isinstance(a, (int, float)): 
            raise ValueError("Has to be a number!")
        self._acc = a

    def get_accumulator(self):
        return self._acc
    
    def add(self, x):
        self._acc += x

    def substract(self, x):
        self._acc -= x

    def multiply(self, x):
        self._acc *= x

    def divide(self, x):
        if x == 0:
            print("Cannot be divided by zero!")
        else: self._acc /= x

    def print_result(self):
        print(f"Result: {self._acc}")

class Sci_calc(Calculator):
    def __init__(self, acc=0.0) -> None:
        super().__init__(acc)
    
    def square(self):
        return pow(self._acc, 2)
    
    def exp(self, x):
        return pow(self._acc, x)
    
    def factorial(self):
        temp = self._acc
        factorial = 1

        while temp >= 1:
            factorial *= temp
            temp -= 1
        return factorial
    
    def print_result(self):
        print(f"Result: {self._acc:.2e}")


def test_calculator():
    calculator = Calculator()
    calculator.print_result()

    calculator.set_accumulator(25)
    calculator.divide(0)
    calculator.print_result()


def test_sci_calc():
    sci_calc = Sci_calc()
    sci_calc.set_accumulator("hi")
    print(sci_calc.factorial())
    sci_calc.print_result()



   
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

    
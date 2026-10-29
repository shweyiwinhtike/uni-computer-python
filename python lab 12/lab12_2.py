import math

# Add your class Calculator and Sci_calc here
        
    
cal = Calculator()
print("Test calculator:")
print("Start value:", cal.get_accumulator())
cal.set_accumulator(5)
print("Check set:", cal.get_accumulator())
cal.add(5)
print("Check Add:")
cal.print_result()
cal.subtract(4.5)
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

# Test Output:
"""
Test calculator:
Start value: 0.0
Check set: 5.0
Check Add:
Result: 10.0
Check Subtract:
Result: 5.5
Check multiply:
Result: 11.0
Check divide by zero:
Cannot Divide By Zero.
Result: 11.0
Check divide:
Result: 5.5

Test sci_cal:
Start value: 0.0
Check set: 5.0
Check square:
Result: 2.50e+01
Check exp:
Result: 4.00e-02
Check factorial to float:
Cannot Factorial Float.
Result: 4.00e-02
Check factorial to negative:
Cannot Factorial Negative.
Result: -5.00e+00
Check factorial:
Result: 2.40e+01
"""
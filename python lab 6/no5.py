def sum_of_digits(userInput):
    userInput = str(userInput)
    total = 0

    for digit in userInput:
        total = total + int(digit)
    return total

x = int(input("Enter your number: "))
print(sum_of_digits(x))
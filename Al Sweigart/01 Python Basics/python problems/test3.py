# Ask the user for two numbers, then print their sum, product, and remainder

firstQuery = "We ask you of two numbers, and we give you the sum, "
firstQuery += "\nproduct, and remainder of those two numbers!!\n"
print(firstQuery)

firstNumber = int(input("What's your first number? "))
secondNumber = int(input("What's your second number? "))

secondQuery = "\nThe sum of the two numbers is:\n" + str(firstNumber + secondNumber)
secondQuery += "\nThe product of the two numbers is:\n" + str(firstNumber * secondNumber)
secondQuery += "\n The remainder when divide is:\n" + str(firstNumber % secondNumber)

print(secondQuery)

"""
cool note:
When a small number is been divided by a larger number, let's say; 4 / 12, the
remainder is the smaller number. "12 in 4", is 0 remainder 4.
"""

# Write a program that asks the user for their birth year, and prints how old they’ll be in the year 2050.

ask4BirthYear = int(input("What year were you born? "))
yearConstant = 2050
print("You are going to be " + str(yearConstant - ask4BirthYear) + " years old in the year 2050")

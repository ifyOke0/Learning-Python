# Make a program that asks for your name and age, and tells you how many years until you turn 100.
usersName = input("What is your name? ")
usersCurrentAge = int(input("How old are you? "))

query = "Dear " + usersName + " you are not yet 100 years old,"
query += "\nnot until " + str(int(100 - usersCurrentAge)) + " years from now."

print(query)

################# ASSIGNMENT 4 ############
##Write an if-elif-else chain that determines an Individual's stage of life.
##Set a value for the variable age
age = 77

# If the person is less than 2 years old, print a message that the person is a baby.
if age < 2:
    print("Aww, a baby")
# If the person is at least 2 years old but less than 4, print a message that the person is a toddler
elif age < 4:
    print("Aww, you're a toddler now")
# If the person is at least 4 years old but less than 13, print a message that the person is a kid
elif age < 13:
    print("You're a kid!")
# If the person is at least 13 years old but less than 20, print a message that the person is a teenager
elif age < 20:
    print("You're now a teenager")
# If the person is at least 20 years but less than 65, print a message that the person is an adult
elif age < 65:
    print("You should know better, you're now an adult!")
# If the person is age 65 or older, print a message that the person ia an elder
elif age >= 65:
    print("You're now an Elder, Respect")
print("All good ✌")  #The End

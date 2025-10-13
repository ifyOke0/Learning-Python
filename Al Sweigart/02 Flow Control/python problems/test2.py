# Create a "password strength" tester:
# ask for a password, and print whether it's "weak", "medium", or "strong" based on its length

while True:
    password = input("What is your password: ")
    if len(password) >= 8:
        print("STRONG PASSWORD!")
        break
    elif len(password) == 7:
        print("Medium Strength!, input stronger password!")
    elif len(password) < 7:
        print("WEAK!!!, this password is weak.")

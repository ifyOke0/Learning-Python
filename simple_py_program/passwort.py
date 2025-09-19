##### Practice 4
## Simple Password Checker

password = input("Passwort eingeben: ")
has_number = any(char.isdigit() for char in password)

if len(password) > 8 and has_number:
    print("starkes Passwort")
else:
    print("schwaches Passwort! Versuch es noch einmal...")

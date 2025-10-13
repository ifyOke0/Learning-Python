##### Practice 4
## Simple Password Checker
while True:
    passwort = input("Passwort eingeben: ")
    hat_nummer = any(char.isdigit() for char in passwort)
    if len(passwort) >= 8 and hat_nummer:
        print("STARKES PASSWORT!")
        break
    elif len(passwort) == 7 and hat_nummer:
        print("Mittlere Stärke, geben Sie ein stärkeres Passwort ein!")
    elif len(passwort) < 7 and hat_nummer:
        print("SCWACHES PASSWORT!!! Versuch es noch einmal...")
    else:
        print("Passwort eingeben, oder versuchen Sie es mit Nummer!")

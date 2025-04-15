#####Practice 4
##Simple Password Checker
Passwort_prüfen = input("Passwort eingeben: ")
hat_Nummer = any(char.isdigit() for char in Passwort_prufen)

if len(Passwort_prüfen) > 8 and hat_Nummer:
    print("starkes Passwort")
else:
    print("schwaches Passwort!, Versuch es noch einmal...")
###Practice 1
###Grundrechner
zahl1 = float(input("Gib die erste Zahl ein: "))
operand = input("Operator (+,-,*,/): ")
zahl2 = float(input("Gib die zweite Zahl: "))

if operand == "+":
    ergebnis = zahl1 + zahl2
elif operand == "-":
    ergebnis = zahl1 - zahl2
elif operand == "*":
    ergebnis = zahl1 * zahl2
elif operand == "/":
    if zahl2 != 0:
        ergebnis = zahl1 / zahl2
    else:
        ergebnis = "Teilen durch Null(0) is nicht erlaubt"
else:
    ergebnis = "Syntaxfehler!"

print("Ergebnis:", ergebnis)

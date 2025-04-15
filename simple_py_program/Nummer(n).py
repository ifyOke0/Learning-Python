###Practice 6
##Lies eine Zahl (n) und gib die Reihe(series) aus "1+2+...+n="
n = int(input("Gib die eine Nummer ein: "))

reihe = " + ".join(str(i) for i in range(1, n + 1))
summe = sum(range(1, n + 1))

print(f"{reihe} = {summe}")
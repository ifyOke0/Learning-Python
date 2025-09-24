#####Practice 3
##Rate Nummer  
import random

Geheim_nummer = random.randint(1, 10)
rate = None

while rate != Geheim_nummer:
    rate = int(input("Errate die Nummer (1-10): "))

    if rate < Geheim_nummer:
        print("Zu niedrig!")
    elif rate > Geheim_nummer:
        print("Zu hoch!")
    else:
        print("Richtig, die Geheim_nummer war ", Geheim_nummer)

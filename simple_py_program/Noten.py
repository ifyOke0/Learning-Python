###Practice 5
##Schülernoten

Schüler_info = {
    "Henry": 85,
    "Esther": 99,
    "Jane": 100,
    "Emmanuel": 83,
    "Miracle": 91,
    "Precious": 79
}

for schüler, noten in Schüler_info.items():
     print(f"{schüler}: {noten}")
     Durchschnitt1 = noten / len(Schüler_info)
     print(Durchschnitt1)

durchschnitt = sum(Schüler_info.values()) / len(Schüler_info)
print("Durchschnittliche Note:", durchschnitt)





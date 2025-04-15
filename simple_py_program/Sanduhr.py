def Sanduhr_muster(n):
    # Die Reichweite.
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)
    for i in range(2, n, 1):
        print(" " * (n - i) + "* " * i)

output = ""  

# Capture output into the variable
for i in range(5, 0, -1):
    output += " " * (5 - i) + "* " * i + "\n"
for i in range(2, 5):
    output += " " * (5 - i) + "* " * i + "\n"

# Save output to the root folder
with open("output_Sanduhr.md", "w", encoding="utf-8") as f:
    f.write("```\n" + output + "```\n")

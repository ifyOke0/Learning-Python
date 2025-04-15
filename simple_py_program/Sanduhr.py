def Sanduhr_muster(n):
    output = ""
    
    for i in range(n, 0, -1):
        output += " " * (n - i) + "* " * i + "\n"

    for i in range(2, n, 1):
        output += " " * (n - i) + "* " * i + "\n"
    
    return output

output = Sanduhr_muster(5)

with open("output_Sanduhr.md", "w", encoding="utf-8") as f:
    f.write("```\n" + output + "```\n")


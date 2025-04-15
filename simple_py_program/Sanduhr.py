import os

def Sanduhr_muster(n):
    lines = []
    for i in range(n, 0, -1):
        lines.append(" " * (n - i) + "* " * i)
    for i in range(2, n + 1):
        lines.append(" " * (n - i) + "* " * i)
    return "\n".join(lines)

output = Sanduhr_muster(5)
print(output)


repo_root = os.path.dirname(os.path.abspath(__file__))  
output_path = os.path.join(repo_root, "output_Sanduhr.md")

with open(output_path, "w", encoding="utf-8") as f:
    f.write("```\n" + output + "\n```")

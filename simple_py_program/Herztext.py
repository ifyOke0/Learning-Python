import os

output = '\n'.join(
    [''.join(
        [(' Pride  '[(x - y) % 8] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 -
         (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ')
         for x in range(-30, 30)])
     for y in range(15, -15, -1)]
)

print(output)

# Save output to root directory
repo_root = os.path.dirname(os.path.abspath(__file__))  # Herztext is in root
output_path = os.path.join(repo_root, "output_Herztext.md")

with open(output_path, "w", encoding="utf-8") as f:
    f.write("```\n" + output + "\n```")

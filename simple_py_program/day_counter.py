import datetime
import os

start_date = datetime.date(2025, 5, 13)

today = datetime.date.today()

# Calculate the number of days between today and the start date
days = (today - start_date).days + 1
days = max(0, min(days, 100))

line_text = f"Day {days} of Python Coding"

# Paths
script_dir = os.path.dirname(os.path.abspath(__file__))
readme_path = os.path.join(script_dir, "..", "README.md")

# Read and replace in README
with open(readme_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

with open(readme_path, "w", encoding="utf-8") as f:
    inside_block = False
    for line in lines:
        if "<!-- PYTHON_DAY_COUNTER -->" in line:
            f.write(line)
            f.write(line_text + "\n")
            inside_block = True
        elif "<!-- PYTHON_DAY_COUNTER_END -->" in line:
            inside_block = False
            f.write(line)
        elif not inside_block:
            f.write(line)

import os
from datetime import datetime

# === CONFIGURATION ===
start_date = datetime(2025, 5, 13)
max_days = 100

# === CALCULATE DAY ===
today = datetime.now()
days_passed = (today - start_date).days + 1

if days_passed > max_days:
    day_message = f"Day {max_days} of Python Coding"
elif days_passed < 1:
    day_message = "Day 0 of Python Coding"
else:
    day_message = f"Day {days_passed} of Python Coding"

# === LOCATE README ===
# This gets the parent directory of the script
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
readme_path = os.path.join(parent_path, "README.md")

# === UPDATE README.md ===
start_tag = "<!-- PYTHON_DAY_COUNTER -->"
end_tag = "<!-- PYTHON_DAY_COUNTER_END -->"

with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

# Replaces content between the start and end tags
before = readme_content.split(start_tag)[0] + start_tag + "\n"
after = "\n" + end_tag + readme_content.split(end_tag)[1]
new_content = before + day_message + after

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("README.md updated with:", day_message)

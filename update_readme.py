from datetime import datetime

README_FILE = "README.md"

start_date = datetime(2025, 4, 13)
today = datetime.now()

# Calculate days
days_learning = (today - start_date).days + 1  # +1 to include the start day

# Cap the day at 100
if days_learning > 100:
    days_learning = 100

# New day counter text
new_day_line = f"✨ Day {days_learning} of learning Python ✨"

# New progress bar URL
progress_url = f"https://progress-bar.dev/{days_learning}/?title=Progress&width=500"

# Update the README
with open(README_FILE, "r", encoding="utf-8") as file:
    lines = file.readlines()

with open(README_FILE, "w", encoding="utf-8") as file:
    for line in lines:
        if "Day" in line and "of learning Python" in line:
            file.write(new_day_line + "\n")
        elif "https://progress-bar.dev/" in line:
            file.write(f"![Progress]({progress_url})\n")
        else:
            file.write(line)
from datetime import date
import subprocess
today = date.today()
filename = today.strftime("%B %d") + ".md"
try:
    with open(filename, "x") as f:
        f.write(
            "---\n"
            "title: Quantifiers\n"
            "date: " + today.strftime("%B %d, %Y") + "\n"
            "author: Dhruva Sambrani\n"
            "---"
        )
except IOError:
    pass
finally:
    subprocess.call(['atom', filename, "--dir=\".\""], shell=True)

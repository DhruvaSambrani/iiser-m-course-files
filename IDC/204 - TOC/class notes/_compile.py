import subprocess
import webbrowser
from datetime import date
today = date.today()
md = today.strftime("%B %d") + ".md"
pdf = today.strftime("%B %d") + ".pdf"
subprocess.call(['pandoc',
                 "-s",
                 md,
                 "-f",
                 "markdown",
                 "--pdf-engine",
                 "xelatex",
                 "--variable=mainfont:Cambria Math",
                 "-o",
                 pdf],
                shell=True)
recipient = "shane@iisermohali.ac.in"
subject = "Class Notes for " + today.strftime("%B %d")
subject = subject.replace(' ', '%20')
body = "Please find attached."
body = body.replace(' ', '%20')
webbrowser.open(
    'mailto:?to=' +
    recipient +
    '&subject=' +
    subject +
    '&body=' +
    body,
    new=1)

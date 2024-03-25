from pathlib import Path

path = Path("git_cheatsheet.txt")

if(path.exists()):
    content = path.read_text()
    print(content.upper())
else:
    print("File does not exist")

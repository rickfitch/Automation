from pathlib import Path

path = Path("hello.txt")

if(path.exists()):
    content = path.read_text()
    print(content.upper())
else:
    print("File does not exist")

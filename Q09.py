# Q09: Display lines containing a particular word.
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("Python is fun.\nFiles store data.\nPython reads files.\n", encoding="utf-8")
word=input("Word to search: ")
for line in p.read_text(encoding="utf-8").splitlines():
    if word.lower() in line.lower(): print(line)

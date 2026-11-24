# Q34: Count occurrences of a particular word in a file.
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("Python is fun. Python is useful.",encoding="utf-8")
word=input("Word: "); words=p.read_text(encoding="utf-8").lower().split(); print("Occurrences:",words.count(word.lower()))

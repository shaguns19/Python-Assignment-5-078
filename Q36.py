# Q36: Find the longest word in a text file.
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("Python programming file handling",encoding="utf-8")
words=p.read_text(encoding="utf-8").split(); print("Longest word:",max(words,key=len) if words else "No words")

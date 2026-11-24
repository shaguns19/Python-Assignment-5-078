# Q35: Search for a word in a file and report whether it exists.
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("Python is useful.",encoding="utf-8")
word=input("Search word: "); found=word.lower() in p.read_text(encoding="utf-8").lower().split()
print("Word found." if found else "Word not found.")

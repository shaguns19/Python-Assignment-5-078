# Q03: Read the first 10 characters.
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("Python file handling demo.\n", encoding="utf-8")
with open(p,"r",encoding="utf-8") as f: print(f.read(10))

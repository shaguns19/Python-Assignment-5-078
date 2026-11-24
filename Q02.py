# Q02: Read the entire contents using read().
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("Python file handling demo.\n", encoding="utf-8")
with open(p,"r",encoding="utf-8") as f: contents=f.read()
print(contents)

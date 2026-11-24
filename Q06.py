# Q06: Count characters in a text file.
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("Count these characters.\n", encoding="utf-8")
text=p.read_text(encoding="utf-8")
print("Characters:",len(text))

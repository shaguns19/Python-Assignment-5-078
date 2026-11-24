# Q07: Count lines in a text file.
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("One\nTwo\nThree\n", encoding="utf-8")
with open(p,"r",encoding="utf-8") as f: print("Lines:",sum(1 for _ in f))

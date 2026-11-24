# Q05: Read all lines using readlines().
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("First line\nSecond line\n", encoding="utf-8")
with open(p,"r",encoding="utf-8") as f: lines=f.readlines()
for line in lines: print(line,end="")

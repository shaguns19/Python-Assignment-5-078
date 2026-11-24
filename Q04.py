# Q04: Read a file line by line using readline().
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("First line\nSecond line\nThird line\n", encoding="utf-8")
with open(p,"r",encoding="utf-8") as f:
    line=f.readline()
    while line: print(line,end=""); line=f.readline()

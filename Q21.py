# Q21: Demonstrate read mode (r).
from pathlib import Path
p=Path("read_demo.txt")
if not p.exists(): p.write_text("Read mode sample.\n",encoding="utf-8")
with open(p,"r",encoding="utf-8") as f: print(f.read())

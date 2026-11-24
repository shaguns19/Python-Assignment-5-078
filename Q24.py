# Q24: Demonstrate read/write mode (r+).
from pathlib import Path
p=Path("rplus_demo.txt")
if not p.exists(): p.write_text("Original content.\n",encoding="utf-8")
with open(p,"r+",encoding="utf-8") as f:
    print("Before:",f.read()); f.seek(0); f.write("Updated")
print("r+ reads and writes without truncating the file.")

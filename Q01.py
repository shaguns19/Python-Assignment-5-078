# Q01: Read an existing text file and display its contents.
from pathlib import Path
p = Path("sample.txt")
if not p.exists(): p.write_text("Hello from the sample text file!\n", encoding="utf-8")
with p.open("r", encoding="utf-8") as f: print(f.read())

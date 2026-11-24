# Q08: Count words in a text file.
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("Count the words in this file.\n", encoding="utf-8")
print("Words:",len(p.read_text(encoding="utf-8").split()))

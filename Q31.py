# Q31: Count vowels in a text file.
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("Python programming",encoding="utf-8")
text=p.read_text(encoding="utf-8").lower(); print("Vowels:",sum(ch in "aeiou" for ch in text))

# Q33: Count digits and special characters in a file.
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("Python 3.13!",encoding="utf-8")
text=p.read_text(encoding="utf-8"); digits=sum(c.isdigit() for c in text); special=sum(not c.isalnum() and not c.isspace() for c in text)
print("Digits:",digits); print("Special characters:",special)

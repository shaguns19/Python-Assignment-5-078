# Q32: Count uppercase and lowercase letters in a file.
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("Python File",encoding="utf-8")
text=p.read_text(encoding="utf-8"); print("Uppercase:",sum(c.isupper() for c in text)); print("Lowercase:",sum(c.islower() for c in text))

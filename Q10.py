# Q10: Display file lines in reverse order.
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("First\nSecond\nThird\n", encoding="utf-8")
for line in reversed(p.read_text(encoding="utf-8").splitlines()): print(line)

# Q37: Display lines beginning with a specified character.
from pathlib import Path
p=Path("sample.txt")
if not p.exists(): p.write_text("Apple\nBanana\nAvocado\n",encoding="utf-8")
ch=input("Starting character: ")
for line in p.read_text(encoding="utf-8").splitlines():
    if line.startswith(ch): print(line)

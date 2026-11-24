# Q38: Convert lowercase letters in a file to uppercase in another file.
from pathlib import Path
src=Path("lowercase.txt")
if not src.exists(): src.write_text("Convert this text.\n",encoding="utf-8")
Path("uppercase.txt").write_text(src.read_text(encoding="utf-8").upper(),encoding="utf-8")
print("Converted text saved to uppercase.txt")

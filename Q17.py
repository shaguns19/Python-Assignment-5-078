# Q17: Copy one text file to another.
from pathlib import Path
src=Path("source.txt")
if not src.exists(): src.write_text("Copy this text.\n",encoding="utf-8")
Path("copy.txt").write_text(src.read_text(encoding="utf-8"),encoding="utf-8")
print("Copied source.txt to copy.txt")

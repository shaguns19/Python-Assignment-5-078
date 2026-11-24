# Q40: Merge two files into a third file.
from pathlib import Path
p1=Path("file1.txt"); p2=Path("file2.txt")
if not p1.exists(): p1.write_text("Contents of file one.\n",encoding="utf-8")
if not p2.exists(): p2.write_text("Contents of file two.\n",encoding="utf-8")
Path("merged.txt").write_text(p1.read_text(encoding="utf-8")+p2.read_text(encoding="utf-8"),encoding="utf-8")
print("Merged into merged.txt")

# Q39: Reverse character order and write into another file.
from pathlib import Path
src=Path("reverse_source.txt")
if not src.exists(): src.write_text("Reverse this text!",encoding="utf-8")
Path("reversed_chars.txt").write_text(src.read_text(encoding="utf-8")[::-1],encoding="utf-8")
print("Reversed contents saved.")

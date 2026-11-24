# Q42: Display filename and available information.
from pathlib import Path
p=Path(input("Enter file path: "))
if p.exists(): print("Name:",p.name,"\nPath:",p.resolve(),"\nSize (bytes):",p.stat().st_size,"\nSuffix:",p.suffix)
else: print("Path does not exist.")

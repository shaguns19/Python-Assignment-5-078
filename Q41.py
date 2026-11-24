# Q41: Check whether a specified file exists.
from pathlib import Path
name=input("Filename to check: "); print("Exists" if Path(name).is_file() else "File does not exist")

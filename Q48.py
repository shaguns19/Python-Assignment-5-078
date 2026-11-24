# Q48: Demonstrate os.path.exists() and os.path.getsize().
import os
path=input("Enter path: ")
if os.path.exists(path): print("Exists: True", "\nSize (bytes):",os.path.getsize(path))
else: print("Path does not exist.")

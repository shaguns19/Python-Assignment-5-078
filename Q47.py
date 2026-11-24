# Q47: Check whether a path represents a file or directory.
import os
path=input("Enter path: ")
if os.path.isfile(path): print("This is a file.")
elif os.path.isdir(path): print("This is a directory.")
else: print("Path does not exist or is neither.")

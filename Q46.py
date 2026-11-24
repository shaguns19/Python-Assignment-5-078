# Q46: Display all filenames in a specified directory.
import os
path=input("Directory path (blank for current directory): ") or "."
if os.path.isdir(path):
    for name in os.listdir(path): print(name)
else: print("Directory not found.")

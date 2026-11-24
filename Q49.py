# Q49: Rename a text file then display its contents.
import os
old=input("Existing text filename: "); new=input("New filename: ")
if os.path.isfile(old):
    os.rename(old,new)
    with open(new,"r",encoding="utf-8") as f: print(f.read())
else: print("File not found.")

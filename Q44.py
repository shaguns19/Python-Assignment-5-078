# Q44: Delete an existing file using os.
import os
name=input("File to delete: ")
if os.path.isfile(name): os.remove(name); print("Deleted.")
else: print("File not found.")

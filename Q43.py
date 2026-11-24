# Q43: Rename an existing file using os.
import os
old=input("Existing filename: "); new=input("New filename: ")
if os.path.isfile(old): os.rename(old,new); print("Renamed.")
else: print("File not found.")

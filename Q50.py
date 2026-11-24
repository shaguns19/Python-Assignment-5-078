# Q50: Create, write, read, close and delete a file.
import os
name="temporary_demo.txt"
f=open(name,"w",encoding="utf-8"); f.write("This file will be read and then deleted.\n"); f.close()
f=open(name,"r",encoding="utf-8"); print(f.read()); f.close(); print("Closed:",f.closed)
os.remove(name); print("Temporary file deleted.")

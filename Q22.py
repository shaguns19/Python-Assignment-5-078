# Q22: Demonstrate write mode (w).
with open("write_demo.txt","w",encoding="utf-8") as f: f.write("This is written using write mode.\n")
print("File written (write mode replaces previous contents).")

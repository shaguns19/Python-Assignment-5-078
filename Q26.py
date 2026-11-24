# Q26: Demonstrate append/read mode (a+).
with open("aplus_demo.txt","a+",encoding="utf-8") as f:
    f.write("Added line.\n"); f.seek(0); print(f.read())

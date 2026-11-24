# Q25: Demonstrate write/read mode (w+).
with open("wplus_demo.txt","w+",encoding="utf-8") as f:
    f.write("Written and then read.\n"); f.seek(0); print(f.read())

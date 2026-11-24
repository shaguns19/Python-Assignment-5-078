# Q29: Read a file from a specified pointer position.
with open("position_demo.txt","w+",encoding="utf-8") as f:
    f.write("0123456789"); position=int(input("Start position (0–9): ")); f.seek(position); print(f.read())

# Q28: Change file pointer position using seek().
with open("seek_demo.txt","w+",encoding="utf-8") as f:
    f.write("ABCDEFGH"); f.seek(3); print("From position 3:",f.read())

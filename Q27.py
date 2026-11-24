# Q27: Display current file pointer using tell().
with open("pointer_demo.txt","w+",encoding="utf-8") as f:
    f.write("Python"); print("After writing:",f.tell()); f.seek(0); print("After seek(0):",f.tell()); f.read(3); print("After reading 3:",f.tell())

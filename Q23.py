# Q23: Demonstrate append mode (a).
with open("append_demo.txt","a",encoding="utf-8") as f: f.write("Appended line.\n")
print("Line appended to append_demo.txt")

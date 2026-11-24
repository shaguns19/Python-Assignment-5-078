# Q15: Append text to an existing file.
with open("notes.txt","a",encoding="utf-8") as f: f.write(input("Text to append: ")+"\n")
print("Text appended.")

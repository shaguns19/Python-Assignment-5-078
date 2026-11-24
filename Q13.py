# Q13: Write multiple lines using writelines().
lines=["Line one\n","Line two\n","Line three\n"]
with open("lines.txt","w",encoding="utf-8") as f: f.writelines(lines)
print("Lines written.")

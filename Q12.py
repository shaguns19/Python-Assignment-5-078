# Q12: Write five student names to a text file.
names=[input(f"Enter student name {i+1}: ") for i in range(5)]
with open("students.txt","w",encoding="utf-8") as f: f.write("\n".join(names)+"\n")
print("Names saved.")

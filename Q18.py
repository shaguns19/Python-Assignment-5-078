# Q18: Write student details to a file.
name=input("Name: "); roll=input("Roll number: "); marks=input("Marks: ")
with open("student_details.txt","w",encoding="utf-8") as f: f.write(f"Name: {name}\nRoll number: {roll}\nMarks: {marks}\n")
print("Details saved.")

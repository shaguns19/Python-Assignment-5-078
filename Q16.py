# Q16: Demonstrate write mode vs append mode.
with open("mode_demo.txt","w",encoding="utf-8") as f: f.write("Write mode replaces existing content.\n")
with open("mode_demo.txt","a",encoding="utf-8") as f: f.write("Append mode adds to the end.\n")
print(open("mode_demo.txt",encoding="utf-8").read())

# Q20: Store first 100 natural numbers in a file.
with open("natural_numbers.txt","w",encoding="utf-8") as f: f.write("\n".join(map(str,range(1,101)))+"\n")
print("Numbers 1–100 saved.")

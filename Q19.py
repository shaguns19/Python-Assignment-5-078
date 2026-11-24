# Q19: Store a multiplication table in a text file.
n=int(input("Enter number: "))
with open("table.txt","w",encoding="utf-8") as f:
    for i in range(1,11): f.write(f"{n} x {i} = {n*i}\n")
print("Table saved.")

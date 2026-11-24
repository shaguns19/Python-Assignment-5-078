# Q14: Accept text and store it in a file.
text=input("Enter text to save: ")
with open("user_text.txt","w",encoding="utf-8") as f: f.write(text+"\n")
print("Saved to user_text.txt")

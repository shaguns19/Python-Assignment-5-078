# Q30: Demonstrate close() and check whether file is closed.
f=open("close_demo.txt","w",encoding="utf-8"); f.write("Closing file example."); f.close(); print("Is closed?",f.closed)

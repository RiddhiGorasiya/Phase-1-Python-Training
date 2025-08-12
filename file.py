# # # # #open, read & close file 

f = open("PHASE 1\demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close

# # # # reading a file

f = open("PHASE 1\demo.txt","r")
data = f.read(6)
print(data)
print(type(data))
f.close

f = open("PHASE 1\demo.txt","r")
line1 = f.readline()
print(line1)
f.close

# # # writing a file

f = open("PHASE 1\demo.txt","w")
f.write("I want to learn Javascript tomorrow.")
f.close

f = open("PHASE 1\demo.txt","a")
f.write("Then I'll move to ReactJS.")
f.write("\n After that node.js.")
f.close 

# # with systax

with open("PHASE 1\demo.txt", "r") as f:
    data = f.read()
    print(data)

# deletina a file

import os
os.remove("PHASE 1\sample.txt")
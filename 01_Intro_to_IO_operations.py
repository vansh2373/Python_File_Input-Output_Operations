"""
File Reading 
"""

f = open(r"C:\Users\arora\OneDrive\Desktop\File.txt")
data = f.read()
print(data)
f.close()

"""
File Writing 
"""
st = "Hi you are amazing."

f = open("MyFile.txt","w")
f.write(st)
f.close()


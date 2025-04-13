"""
f = open(r"C:\Users\arora\OneDrive\Documents\GitHub\Python_File_Input-Output_Operations\MyFile.txt")
print(f.read())
f.close()
"""

# The same can be written using with statement like this 

with open(r"C:\Users\arora\OneDrive\Documents\GitHub\Python_File_Input-Output_Operations\MyFile.txt") as f:
    print(f.read())

# you dont have to explicitly close the file


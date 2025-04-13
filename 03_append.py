"""
Append Mode in file I/O
"""

st = "Hey Vansh!"

f = open(r"C:\Users\arora\OneDrive\Documents\GitHub\Python_File_Input-Output_Operations\MyFile.txt","a")
f.write("\n"+st)
f.close()
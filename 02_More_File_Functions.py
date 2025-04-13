"""
writing a file
"""
# f = open("MoreFunctionsFile.txt","w")
# f.write("""Hi You are Amazing
#            This is second Line
#             This is Third line
#             This is Fourth Line """)
# f.close()

"""
readlines function
"""

# data = open(r"C:\Users\arora\OneDrive\Documents\GitHub\Python_File_Input-Output_Operations\MoreFunctionsFile.txt")
# lines = data.readlines()
# print(lines,type(lines))
# data.close()

"""
Readline Function used for reading single line at a time
"""
file1 = open(r"C:\Users\arora\OneDrive\Documents\GitHub\Python_File_Input-Output_Operations\MoreFunctionsFile.txt")
line1 = file1.readline()
print(line1,type(line1))

line2 = file1.readline()
print(line2,type(line2))

line3 = file1.readline()
print(line3,type(line3))

line4 = file1.readline()
print(line4,type(line4))

file1.close()


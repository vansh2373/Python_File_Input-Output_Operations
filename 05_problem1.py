"""
There is a file poems.txt read it and find out if it contains word twinkle or not!
"""

with open("poems.txt","r") as f:
    content = f.read()
    if ("twinkle" in content):
        print("The word twinkle is present in the content")
    else:
        print("The word twinkle is not present in the content")

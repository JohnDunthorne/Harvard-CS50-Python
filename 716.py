# now we will read a file with file I/O

with open("names.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    print("Hello,", line, end="")
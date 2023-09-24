# now we will read a file with file I/O

with open("names.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    print("Hello,", line.rstrip())

# we can shorten all this in python

with open("names.txt", "r") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())

# I sorted for good measure
# now we will read a file with file I/O

with open("names.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    print("Hello,", line.rstrip())

# we can shorten all this in python
# we can leave out "r" as an arguement
# as it is set to the default
# if nothing is there
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())

# I sorted for good measure
# use file I/O to read and write stored memory

name = input("Whats your name: ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# This is a better way to do this in python
# than what we did in 710.py    
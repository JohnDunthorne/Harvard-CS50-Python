# use file I/O to read and write stored memory

name = input("Type your name: ")
# "a" as a second argument will append
# to the file, so we can add to it
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
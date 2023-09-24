# use file I/O to read and write stored memory

name = input("Type your name: ")

# open a file that youd like to save
# the name to,
# we write "w" as a second argument
# to let python know we are writing
# to the file
file = open("names.txt", "w")
# we assign open a variable so we can
# handle it.

# Write the selected variable to the file
file.write(name)

# Then close the file so we can save our name
file.close()

# This code as its stands will overwrite
# the original .txt file each time though
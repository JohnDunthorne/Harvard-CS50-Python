# Ask user for their name
name = input("name: ")

# Remove white space from str
name = name.strip()

# Make sure name is capitalised properly
name = name.capitalize()

# Say hello to user
print("hello " + name)
print("hello", name)
print(f"hello \"{name}\"")

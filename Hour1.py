# Ask user for their name
name = input("name: ")

# Remove white space from str
name = name.strip()

# Make sure name is capitalised properly
name = name.capitalize()

# Perhaps it'll be a 1st and 2nd name input for capitalization
name = name.title()

# Put several methods on just one line
name = name.strip().title()

# Put methods at the end of the original variable
name = input("Name: ").strip().title()

# Say hello to user
print("hello " + name)
print("hello", name)
print(f"hello \"{name}\"")

# Ask user for their name
name = input("Name: ").strip().title()

# Split user name into first and last name
first, last = name.split()

# Say hello to user "Sarcastically" ;)
print(f"Hello \"{name}\"")
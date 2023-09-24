# use file I/O to read and write stored memory

# collect 3 names from user input
names = []

for _ in range(3):
    name = input("Type your name: ")
    names.append(name)

# Sort names alphabetically
for name in sorted(names):
    print(f"hello, {name}")
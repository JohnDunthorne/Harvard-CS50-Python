# Make a cat meow again using a for loop

for meow in [0, 1, 2]:
    print("Meow")

# A better way to represent this is with range function

for _ in range(3):
    print("MEOW") 

# use _ for a variable you'll never use again

# aside from for loop you could just do this

print("meow\n" * 3, end="")      
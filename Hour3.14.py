# meow based on user input

# get user input of a positive integer

while True:
    n = int(input("select a nummber: "))
    if n <= 0:
        continue
    else:
        break

# we could tighten up this code like this

while True:
    n = int(input("select a nummber: "))
    if n > 0:
        break

# Create the meow for loop  
    
for _ in range(n):
    print("Meow")
# Prompt the user to provide a number, until they do.

while True:
    try:
        x =  int(input("Pick a number: "))
    except ValueError:
        print("Please only type a number")
    else: 
        break   
        
        
print(f"x is {x}")
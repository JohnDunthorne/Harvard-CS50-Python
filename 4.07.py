# Create an exception to fix

# our exception is writing a str in an int input

try:
    x =  int(input("Pick a number: "))
except ValueError:
    print("Please only type a number")
else:    
    print(f"x is {x}")
# create a function that says hello

def HelloFunction():
    print("hello")


HelloFunction()  

# Create a function that can receive an input
# then print hello to the user

def HelloUser(to):
    print("Hello,", to)

HelloUser(input("What's your name? ").title().strip())



# create a function that says hello

def hello_function():
    print("hello")


hello_function()  

# Create a function that can receive an input
# then print hello to the user
# .title() .strip etc.

def hello_user(to):
    print("Hello,", to)

def main():
 hello_user(input("What's your name? ").title().strip())

main()



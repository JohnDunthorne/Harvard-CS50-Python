# Create your own fuction for checking if a
# number is even

def main():
    x = int(input("Choose a number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False
# you could also write
# **return n % 2 == 0**, since its a boolean
    
main()    
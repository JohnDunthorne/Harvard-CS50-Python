# Have a function return a value

def main():
    x = int(input("Select number: "))
    print(f"{x} squared is {square(x)}")

def square(n):
    n *= n
    return n 

main()   

# Create a function for meowing

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Choose a number: "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()

                          
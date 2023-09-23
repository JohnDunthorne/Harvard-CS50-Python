# Square a number based on user input

from functions import square

def main():
    x = int(input("Select a number: "))
    print(square(x))

# this code below ensures
# main only gets called
# when this file is ran
# not if functions are
# imported somewhere else

if __name__ == "__main__":
    main()
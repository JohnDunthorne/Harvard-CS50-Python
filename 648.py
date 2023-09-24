# Test this code (See 649.py)

from functions import hello_name

def main():
    name = input("Whats your name: ").strip().capitalize()
    print(hello_name(name))

if __name__ == "__main__":
    main()
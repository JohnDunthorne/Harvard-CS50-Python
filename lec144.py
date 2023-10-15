import sys

def multiply(a, b):
    return a * b

def main():
    if len(sys.argv) != 3:
        print("Try 2 integers in command line")
        sys.exit(1)

    try:
        first_int = int(sys.argv[1])
        second_int = int(sys.argv[2])
    except ValueError:
        print("Error: Both arguments should be valid integers.")
        sys.exit(1)

    result = multiply(first_int, second_int)
    print(f"The result of {first_int} * {second_int} is: {result}")

if __name__ == "__main__":
    main()
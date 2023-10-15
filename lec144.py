import sys

def multiply(a, b):
    return a * b

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <number1> <number2>")
        sys.exit(1)

    first_str, second_str = sys.argv[1], sys.argv[2]

    try:
        first_int = int(first_str)
        second_int = int(second_str)
    except ValueError:
        print("Error: Both arguments should be valid integers.")
        sys.exit(1)

    result = multiply(first_int, second_int)
    print(f"The result of {first_int} * {second_int} is: {result}")

if __name__ == "__main__":
    main()
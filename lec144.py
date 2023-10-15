from sys import argv
from sys import exit

def multiply(a,b):
    result = a * b
    return result

if len(argv) != 3:
    print("Need two integers")
    exit(1)

firststr = argv[1]
secondstr = argv[2]

try:
    firstint = int(firststr)
    secondint = int(secondstr)
except ValueError:
    print("Expected numbers only")

if len(argv) == 3:
    print(multiply(firstint, secondint))
else:
    print("type in 2 numbers")
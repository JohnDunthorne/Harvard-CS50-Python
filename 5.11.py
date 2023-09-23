# Collect user input from the command line

import sys

if len(sys.argv) < 2:
    print("Please add your name")
elif len(sys.argv) > 2:
    print("please provide first name only")
else:
    print("Hello, my name is", sys.argv[1])

# Type ***python 5.11.py John***
# for this to work

# note we are pulling index [1] since the name of the program
# itself is at index [0]
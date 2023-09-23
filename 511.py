# Collect user input from the command line

import sys

# Check for potential errors
if len(sys.argv) < 2:
    sys.exit("Please add your name")
elif len(sys.argv) > 2:
    sys.exit("please provide first name only")

# Run code line
print("Hello, my name is", sys.argv[1])

# Type ***python 5.11.py John***
# for this to work

# note we are pulling index [1] since the name of the program
# itself is at index [0]

# sys.exit will  work like print but then end the program
# this way once python receives the correcty information
# it will run the print function on line 12
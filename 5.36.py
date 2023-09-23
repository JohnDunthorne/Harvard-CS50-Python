# install cowsay
# type *** pip install cowsay***
# in the command line

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])

# this did not work, .cow didnt seem to do anything
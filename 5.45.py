# API's are application programming interface
# *** pip install requests ***

import requests
import sys

# if user does not provide the name of the file and the name of
# a band, then exit the program
if len(sys.argv) != 2:
    sys.exit()

requests.get(https://itunes.apple.comsearch?entity=songs&limit=1&term=sys.argv[1])
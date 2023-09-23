# API's are application programming interface
# *** pip install requests ***
import json
import requests
import sys

# if user does not provide the name of the file and the name of
# a band, then exit the program
if sys.argv != 2:
    sys.exit

response = requests.get("https://itunes.apple.com/search?term=" + sys.argv[1] + "&limit=1.")
print(json.dumps(response.json(), indent=2))

# This url doesnt work now for some reason
# API's are application programming interface
# *** pip install requests ***
import json
import requests
import sys

# if user does not provide the name of the file and the name of
# a band, then exit the program
if len(sys.argv) != 3:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?term=" + sys.argv[1] + "&limit=" + sys.argv[2] + ".")
# print(json.dumps(response.json(), indent=2))

# Write code to print an amount of song names
# that the user types at the prompt
# user must write
# *python* file name, artist, number of songs

jsonlist = response.json()
for song_name in jsonlist["results"]:
    print(song_name["trackName"])
# this is how we pull lines from a csv file

import csv

with open("Tracking.csv", "r") as file:
    reader = csv.DictReader(file)
    landmark, moniker, summit, isl, corp, camp = 0, 0, 0, 0, 0, 0
    for row in reader:
        fav_customer = row["Customer"]
        if fav_customer == "landmark":
            landmark += 1
        elif fav_customer == "moniker":
            moniker += 1
        elif fav_customer == "summit":
            summit += 1
        elif fav_customer == "isl":
            isl += 1
        elif fav_customer == "corp":
            corp += 1
        elif fav_customer == "camp":
            camp += 1 

print(f"landmark {landmark} moniker {moniker} summit {summit} isl {isl} corp {corp} camp {camp}")
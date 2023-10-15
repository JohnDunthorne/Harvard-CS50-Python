# this is how we pull lines from a csv file

import csv

with open("Tracking.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        customer = row["Customer"]
        date_shipped = row["To Shipping"]
        print(customer, date_shipped)
import csv

# Create a dictionary to store counts for each customer
customer_counts = {
    "lanmarx": 0,
    "moniker": 0,
    "summit": 0,
    "isl": 0,
    "corp": 0,
    "camp": 0,
    "turner": 0,
    "tlj mrk": 0,
    "aka mktg": 0,
    "uei": 0,
    "creativitees": 0,
    "brands": 0,
}

with open("Tracking.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        fav_customer = row["Customer"].lower()  # Convert to lowercase
        if fav_customer in customer_counts:
            customer_counts[fav_customer] += 1

# Print the counts for each customer
for customer, count in customer_counts.items():
    print(f"{customer}: {count}")
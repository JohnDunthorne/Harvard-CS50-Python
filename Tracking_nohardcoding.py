import csv
from collections import defaultdict

# Create a defaultdict to store counts for each customer
customer_counts = defaultdict(int)

with open("Tracking.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        fav_customer = row["Customer"].lower()
        customer_counts[fav_customer] += 1

# Print the counts for each customer
for customer, count in customer_counts.items():
    print(f"{customer}: {count}")
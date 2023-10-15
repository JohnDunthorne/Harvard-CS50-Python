import csv
from collections import defaultdict

# Define the name of the CSV file and the target column
csv_file = "Tracking.csv"
target_column = "Customer"  # Replace with the actual column name

# Create a defaultdict to store the counts for each unique item (case-insensitive)
item_counts = defaultdict(int)

# Read the CSV file and count occurrences
with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        item = row[target_column].lower()  # Convert to lowercase
        item_counts[item] += 1

# Print the counts for each unique item (case-insensitive)
for item, count in item_counts.items():
    print(f"{item}: {count}")
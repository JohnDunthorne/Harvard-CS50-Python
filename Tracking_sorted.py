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

# Sort the dictionary items by count in descending order
sorted_items = sorted(item_counts.items(), key=lambda x: x[1], reverse=True)

# Print the counts for each unique item (case-insensitive) in descending order
for item, count in sorted_items:
    print(f"{item}: {count}")
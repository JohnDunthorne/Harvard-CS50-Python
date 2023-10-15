import csv

with open("phonebook.csv", "a") as file:
    name = input("Name: ")
    number = input("number: ")
    
    writer = csv.writer(file)
    writer.writerow([name, number])
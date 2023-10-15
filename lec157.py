people = {
    "John": "Johns number",
    "Brittany": "Brittanys number",
    "Fallon": "Fallons number"
}

name = input("Name: ")
if name in people:
    print(f"number is {people[name]}")
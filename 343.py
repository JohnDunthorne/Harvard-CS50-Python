# Dictionariers with more data

students = [
    {"name": "Hermione", "house": "Griffindor", "patronus" : "Otter"},
    {"name": "Harry", "house": "Griffindor", "patronus" : "Stag"},
    {"name": "Ron", "house": "Griffindor", "patronus" : "Jack Russell"},
    {"name": "Draco", "house": "Slytherin", "patronus" : None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" - ")
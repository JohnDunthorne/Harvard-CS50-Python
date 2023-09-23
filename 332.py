# dictionaries allow you to associate
# something with something else
# like a word, and its meaning
# in python thats
# keys and values

students = {
    "Hermione": "Griffindor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin",
    }

print(students["Hermione"])

# for loops interate over keys in python

for student in students:
    print(student)

# so the above loop returns all the students names

# to return the house as well do this

for student in students:
    print(student, students[student], sep=" - ")
#^ this is not unlike when we did **print(students["Hermione"])**

# remember 'student' will iterate through the dict
# so you can use it as the index  

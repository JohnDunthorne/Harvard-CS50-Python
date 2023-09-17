# sort your name into a house

name = "John"

match name:
    case "Harry" | "Ron" | "Hermione":    
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("You dont go to Hogwarts")
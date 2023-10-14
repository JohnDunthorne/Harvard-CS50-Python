scores = []
error = print("numbers only")
try:
    for i in range(3):
        score = int(input("Score: "))
        scores.append(score)
except ValueError:
    error

try: 
    average = sum(scores)/len(scores)
except ZeroDivisionError:
    error

try:
    if average >= 90:
        print("A")
    elif average >= 80:
        print("B")    
    elif average >= 70:
        print("C")
    elif average >= 60:
        print("D")
    else:
        print("F")
except NameError:
    error

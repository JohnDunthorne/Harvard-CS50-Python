scores = []
try:
    for i in range(3):
        score = int(input("Score: "))
        scores.append(score)
except ValueError or ZeroDivisionError:
    print("Numbers only")

try:    
    average = sum(scores)/len(scores)
except ValueError or ZeroDivisionError:
    print("Numbers only")

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

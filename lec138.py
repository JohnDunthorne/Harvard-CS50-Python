scores = []

for i in range(3):
    score = int(input("Score: "))
    if 0 <= score <= 100:
        scores.append(score)
    else:
        print("Invalid input")
        scores = [-999, -999, -999]
    
average = sum(scores)/len(scores)

if average >= 90:
    print("A")
elif average >= 80:
    print("B")    
elif average >= 70:
    print("C")
elif average >= 60:
    print("D")
elif 0 <= average < 60:
    print("F")    
else:
    print("You did something wrong")

from statistics import mean

scores = [int(input("First score: ")), int(input("Second score: ")), int(input("Third score: "))]
average = mean(scores)

if average > 90:
    print("A")
elif average > 80:
    print("B")    
elif average > 70:
    print("C")
elif average > 60:
    print("D")
else:
    print("F")
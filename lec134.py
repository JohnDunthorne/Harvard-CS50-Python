print("we are making a block any size you want, tell me:")

n1 = int(input("How many high? "))
n2 = int(input("How many wide? "))
for i in range(n1):
    for j in range(n2):
        print("#", end="")
    print()
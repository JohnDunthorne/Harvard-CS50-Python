
def main():

    s = input("do you agree? ")
    s = s.lower()
    if s in ["y", "yes"]:
        print("Agreed")
    elif s in ["n", "no"]:
        print("Not agreed")
    else:
        print("invalid input, try Y or N")
        main()
if __name__ == "__main__":
    main()

    
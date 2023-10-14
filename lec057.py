
def main():

    s = input("do you agree? ")

    if s in ["Y", "y", "Yes", "YES", "yes"]:
        print("Agreed")
    elif s in ["N", "n", "No", "NO", "no"]:
        print("Not agreed")
    else:
        print("invalid input, try Y or N")
        main()
if __name__ == "__main__":
    main()

    
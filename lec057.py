
def main():

    s = input("do you agree? ")

    if s.lower() in ["y", "yes"]:
        print("Agreed")
    elif s.lower() in ["n", "no"]:
        print("Not agreed")
    else:
        print("invalid input, try Y or N")
        main()
if __name__ == "__main__":
    main()

    
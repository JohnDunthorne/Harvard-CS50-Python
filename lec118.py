def main():
    height = get_height()
    for i in range(height):
        print(f"#", i + 1)


def get_height():
    while True:
        try:
            height = int(input("Height: "))
            if height < 0:
                print("Positive numbers only")
            if height > 0:
                return height
        except ValueError:
                print("numbers only please")


if __name__ == "__main__":
    main()
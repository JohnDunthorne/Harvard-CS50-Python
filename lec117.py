def main():
    n = get_int()
    for i in range(n):
        print("#")

def get_int():
    while True:
        n = int(input("Select a number: "))
        if n > 0:
            return n
        
if __name__ == "__main__":
    main()
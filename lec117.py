
def main(n):
    print("#" * n)    




def get_int(n):
    while True:
        n = int(input("Select a number: "))
        if n > 0:
            return n
        
if __name__ == "__main__":
    main()
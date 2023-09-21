# Define a function to get an integer from user

def main():
    user_number = get_int()
    print(f"Your number is {user_number}")


def get_int():
    while True:
        try:
            user_number =  int(input("Pick a number: "))
        except ValueError:
            print("Please only type a number")
        else: 
            break   
    return user_number        

main()
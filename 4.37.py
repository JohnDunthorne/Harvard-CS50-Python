# Define a function to get an integer from user

def main():
    user_number = get_int("Pick a Number: ")
    print(f"Your number is {user_number}")


def get_int(user_prompt):
    while True:
        try:
            user_number = int(input(user_prompt))
        except ValueError:
            pass
        else: 
            return user_number         

main()
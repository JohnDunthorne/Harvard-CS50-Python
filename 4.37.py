# Define a function to get an integer from user
def main():
    get_int()

def get_int():

    while True:
        try:
            user_number =  int(input("Pick a number: "))
        except ValueError:
            print("Please only type a number")
        else: 
            break   
            
            
    print(f"Your number is {user_number}")

main()
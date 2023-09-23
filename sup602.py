# Create some functions you can use elsewhere
def main():
    hello("John")
    goodbye("John")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

# this code below ensures
# main only gets called
# when this file is ran
# not if functions are
# imported somewhere else
if __name__ == "__main__":

    main()

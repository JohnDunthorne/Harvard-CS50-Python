# Simulate a dice roll with random.choice

from random import choice

def main():
    dice_roll()

def dice_roll():    
    print(choice([1, 2, 3, 4, 5, 6]))
    

main()

# this worked but i think its sloppy
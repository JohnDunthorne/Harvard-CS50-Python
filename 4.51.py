# Simulate a dice roll with random.choice

from random import choice

def main(dice_roll):
    dice_roll = dice_roll(dice_roll)
    print(dice_roll)


def dice_roll(dice_roll):    
    return choice([1, 2, 3, 4, 5, 6])

main(dice_roll)

# this worked but i think its sloppy
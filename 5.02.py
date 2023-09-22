# use random.randint to select a random number

from random import randint
from random import shuffle


random_number = randint(1,100)
print(random_number)

# use random shuffle to a list

cards = ["one of hearts", "two of hearts", "three of hearts", "four of hearts", "five of hearts", "six of hearts"]
shuffle(cards)
for card in cards:    
    print(card)

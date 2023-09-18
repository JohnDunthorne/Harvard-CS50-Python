# use a loop to make a cat meow several times

meow_left = 7
while meow_left > 0:
    print("Meow")
    meow_left -= 1

# Below produces the same result
# Counting up from 0 is more conventional
meows_to_go = 0
while meows_to_go < 7:
    print("MEOW")
    meows_to_go += 1    
    
# draw a block with #
def main():
    draw_block(5)
    draw_block2(10)

def draw_block(size):
    # For each row in square
    for i in range(size):
        # For each brink in row
        for j in range(size):
            # Print brink
            print("#", end="")
        # This prints only a new line    
        print()

# end="" to prevent row of j going to a new line
# print() on line 9 to force i to new line

def draw_block2(size):
    for i in range(size):
        print("[I]" * size)

# This is just an alternative way
# Of doing the same thing


main()
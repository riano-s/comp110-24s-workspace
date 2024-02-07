"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730403386"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

P1_input: str = input("Pick a secret boat location between 1 and 4: ")
P1_number: int = int(P1_input)

if P1_number <= 0:
    print("Error! 0 too low!")
    exit()
else:     
    if P1_number > 4:
        print("Error! " + str(P1_number) + " too high!")
        exit()

P2_input: str = input("Guess a number between 1 and 4:")
P2_number: int = int(P2_input)

if P2_number <= 0:
    print("Error! 0 too low!")
    exit()
else: 
    if P2_number > 4:
        print("Error! " + str(P2_number) + " too high!")
        exit()

if P1_number == P2_number:
    if P2_number == 1:
        print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if P2_number == 2:
        print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
    if P2_number == 3:
        print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
    if P2_number == 4:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
    print("Correct! You hit the ship.")
else:
    if P2_number == 1:
        print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if P2_number == 2:
        print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
    if P2_number == 3:
        print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
    if P2_number == 4:
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)
    print("Incorrect! You missed the ship.")



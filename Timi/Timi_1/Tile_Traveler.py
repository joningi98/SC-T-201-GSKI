import random
import csv
import os
# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'


def move(direction, col, row):
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return (col, row)


def is_victory(col, row):
    return col == 3 and row == 1  # (3,1)


def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")


def find_directions(col, row):
    if col == 1 and row == 1:  # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2:  # (1,2)
        valid_directions = NORTH + EAST + SOUTH
    elif col == 1 and row == 3:  # (1,3)
        valid_directions = EAST + SOUTH
    elif col == 2 and row == 1:  # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2:  # (2,2)
        valid_directions = SOUTH + WEST
    elif col == 2 and row == 3:  # (2,3)
        valid_directions = EAST + WEST
    elif col == 3 and row == 2:  # (3,2)
        valid_directions = NORTH + SOUTH
    elif col == 3 and row == 3:  # (3,3)
        valid_directions = SOUTH + WEST
    return valid_directions


def get_coins(col, row):
    retuning_coins = 0
    coins = []
    num = random.randint(0, 9)
    for _ in range(num):
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        location = x, y
        if location in coins:
            num += 1
            continue
        else:
            coins.append(location)
    if (col, row) in coins:
        if len(coins) != 0:
            coins_on_tile = random.randint(1, 6)
            for _ in range(coins_on_tile):
                print("This leaver has {} coins".format(coins_on_tile))
                answer = input("Pull a lever (y/n): ")
                if answer.lower() == 'y':
                    number_of_coins = int(input("enter how many coins you want: "))
                    if number_of_coins == coins_on_tile:
                        retuning_coins += number_of_coins
                        return retuning_coins
                    coins_on_tile -= number_of_coins
                    retuning_coins += number_of_coins

    return 0


def print_coins(coins, total_coins):
    print("You received {:d} coins, your total is now {:d}.".format(coins, total_coins))


def save_game(row, col, total_coins):
    with open("save.csv", "a+") as file:
        if os.stat("save.csv").st_size == 0:
            file.write("{},{},{}".format("row", "col", "coins"))
        file.write("\n{},{},{}".format(row, col, total_coins))


def play():

    victory = False
    row = 1
    col = 1
    total_coins = 0

    valid_directions = NORTH
    print_directions(valid_directions)

    while not victory:
        direction = input("Direction: ").lower()

        if direction == 'q':
            save_game(row, col, total_coins)
            quit()

        if direction not in valid_directions:
            print("Not a valid direction!")
        else:
            col, row = move(direction, col, row)
            victory = is_victory(col, row)
            if victory:
                print("Victory!")
            else:
                coins = get_coins(col, row)
                total_coins += coins
                if coins > 0:
                    print_coins(coins, total_coins)
                valid_directions = find_directions(col, row)
                print_directions(valid_directions)


# The main program starts here
play_again = True
while play_again:
    play()
    again = input("Play again (y/n): ")
    play_again = (again.lower() == 'y')

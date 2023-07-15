import itertools
import random
import os

grid = []

def main():

    for i in range(3):
        grid.append([])
        for _ in range(3):
            grid[i].append(" ")

    resetGrid()

    while (
        checkWinner() == " "
        and checkFreeSpace() != 0
        and (checkWinner() == " " or checkFreeSpace() == 0)
    ):
        displayGrid()
        movePlayer()

        if checkWinner() != " " and checkFreeSpace() != 0:
            break
        moveComputerBot()

    sayWinner(checkWinner())


def resetGrid():
    for i, j in itertools.product(range(3), range(3)):
        grid[i][j] = " "


def displayGrid():
    print("\n")
    print(f" {grid[0][0]} | {grid[0][1]} | {grid[0][2]}")
    print("---|---|---")
    print(f" {grid[1][0]} | {grid[1][1]} | {grid[1][2]}")
    print("---|---|---")
    print(f" {grid[2][0]} | {grid[2][1]} | {grid[2][2]}")


def movePlayer():
    displayGrid()
    while True:
        row = int(input("Row: "))
        column = int(input("Column: "))
        if row in range(1, 4) and column in range(1, 4):
            row -= 1
            column -= 1
            if grid[row][column] == " ":
                grid[row][column] = "X"
                displayGrid()
                break
            else:
                print("This cell is already occupied. Try again.")
        else:
            print("Invalid input. Please enter row and column numbers between 1 and 3.")


def moveComputer():
    while True:
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if grid[row][column] == " ":
            grid[row][column] = "0"
            break


def moveComputerBot():

    for i in range(2):

        if grid[i][0] == grid[i][2] and grid[i][0] == "X":
            grid[i][1] = "0"

        elif grid[i][0] == grid[i][1] and grid[i][0] == "X":
            grid[i][2] == "0"

    for j in range(2):

        if grid[0][j] == grid[2][j] and grid[0][j] == "X":
            grid[1][j] == "0"

        elif grid[0][j] == grid[1][j] and grid[0][j] == "X":
                grid[2][j] == "0"

    if grid[2][2] == " ":
        grid[2][2] == "0"



def checkFreeSpace():
    return 9 - sum(
        grid[i][j] != " " for i, j in itertools.product(range(3), range(3))
    )


def checkWinner():
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != " ":
            return grid[i][0]

    return next(
        (
            grid[0][j]
            for j in range(3)
            if grid[0][j] == grid[1][j] == grid[2][j] != " "
        ),
        grid[0][0] if grid[0][0] == grid[1][1] == grid[2][2] != " " else " ",
    )


def sayWinner(winner):
    if winner == "X":
        print("You win!")
    elif winner == "0":
        print("You lose!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()
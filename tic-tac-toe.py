import itertools
import random


grid = []


def main():
    for i in range(3):
        grid.append([" "] * 3)

    reset_grid()

    while check_winner() == " " and check_free_space() != 0:
        display_grid()
        move_player()

        if check_winner() != " " and check_free_space() != 0:
            break
        move_computer_bot()

    say_winner(check_winner())


def reset_grid():
    for i, j in itertools.product(range(3), range(3)):
        grid[i][j] = " "


def display_grid():
    print("\n")
    print(f" {grid[0][0]} | {grid[0][1]} | {grid[0][2]}")
    print("---|---|---")
    print(f" {grid[1][0]} | {grid[1][1]} | {grid[1][2]}")
    print("---|---|---")
    print(f" {grid[2][0]} | {grid[2][1]} | {grid[2][2]}")


def move_player():
    display_grid()
    while True:
        row = int(input("Row: "))
        column = int(input("Column: "))
        if row in range(1, 4) and column in range(1, 4):
            row -= 1
            column -= 1
            if grid[row][column] == " ":
                grid[row][column] = "X"
                display_grid()
                break
            else:
                print("This cell is already occupied. Try again.")
        else:
            print("Invalid input. Please enter row and column numbers between 1 and 3.")


def move_computer_bot():
    while True:
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if grid[row][column] == " ":
            grid[row][column] = "O"
            break


def check_free_space():
    return 9 - sum(grid[i][j] != " " for i, j in itertools.product(range(3), range(3)))


def check_winner():
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != " ":
            return grid[i][0]

    for j in range(3):
        if grid[0][j] == grid[1][j] == grid[2][j] != " ":
            return grid[0][j]

    if grid[0][0] == grid[1][1] == grid[2][2] != " ":
        return grid[0][0]

    return " "


def say_winner(winner):
    if winner == "X":
        print("You win!")
    elif winner == "O":
        print("You lose!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()

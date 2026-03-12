#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_draw(board):
    """Returns True if all cells are filled and there is no winner."""
    return all(board[row][col] != " " for row in range(3) for col in range(3))

def get_input(prompt):
    """Prompts until the user enters a valid integer in range 0-2."""
    while True:
        try:
            value = int(input(prompt))
            if value not in [0, 1, 2]:
                print("Invalid input. Please enter 0, 1, or 2.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        row = get_input("Enter row (0, 1, or 2) for player " + player + ": ")
        col = get_input("Enter column (0, 1, or 2) for player " + player + ": ")

        if board[row][col] == " ":
            board[row][col] = player

            # BUG 1 FIX: Check winner BEFORE swapping player
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                return

            # BUG 2 FIX: Check for draw after every move
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                return

            # Swap player only after win/draw checks
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

tic_tac_toe()

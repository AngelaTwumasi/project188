import random

def create_board(rows, cols):
    symbols = ["A", "B", "C", "D", "E", "F", "G", "H"]  # Symbols for matching pairs
    random.shuffle(symbols)
    num_pairs = rows * cols // 2
    pairs = symbols[:num_pairs] * 2  # Duplicate symbols to create pairs
    random.shuffle(pairs)
    board = [pairs[i:i+cols] for i in range(0, len(pairs), cols)]
    return board

def print_board(board, revealed):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if revealed[i][j]:
                print(board[i][j], end=" ")
            else:
                print("*", end=" ")
        print()

def select_card():
    row = int(input("Enter row number: ")) - 1
    col = int(input("Enter column number: ")) - 1
    return row, col

def play_game(rows, cols):
    board = create_board(rows, cols)
    revealed = [[False] * cols for _ in range(rows)]
    print("Welcome to Memory Match!")
    print_board(board, revealed)

    matched_pairs = 0
    total_pairs = rows * cols // 2
    attempts = 0

    while matched_pairs < total_pairs:
        print("\nTurn", attempts + 1)
        print_board(board, revealed)
        print("")

        print("Select the first card:")
        row1, col1 = select_card()
        while revealed[row1][col1]:
            print("Card already revealed. Select another one.")
            row1, col1 = select_card()

        print("Select the second card:")
        row2, col2 = select_card()
        while revealed[row2][col2] or (row1 == row2 and col1 == col2):
            print("Card already revealed or same as first card. Select another one.")
            row2, col2 = select_card()

        if board[row1][col1] == board[row2][col2]:
            print("Congratulations! You found a matching pair!")
            matched_pairs += 1
            revealed[row1][col1] = True
            revealed[row2][col2] = True
        else:
            print("Sorry, the cards don't match.")

        attempts += 1

    print("\nCongratulations! You completed the game in", attempts, "attempts.")

if __name__ == "__main__":
    rows = int(input("Enter number of rows for the board: "))
    cols = int(input("Enter number of columns for the board: "))
    play_game(rows, cols)

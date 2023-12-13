def checkBoard(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve_eight_queens(board, row):
    if row == len(board):
        # All queens are placed, print the solution
        for i in range(len(board)):
            for j in range(len(board)):
                print(board[i][j], end=' ')
            print()
        print("\n")
        return

    for col in range(len(board)):
        if checkBoard(board, row, col):
            board[row][col] = 1
            solve_eight_queens(board, row + 1)
            board[row][col] = 0  # Backtrack


def eight_queens():
    n = 8  # Size of the chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_eight_queens(board, 0)


if __name__ == "__main__":
    eight_queens()

def print_board(board):
    for row in board[::-1]:
        for element in row:
            print(element, end=" ")
        print()

def initialize_board(num_rows, num_cols):
    return[["-" for j in range(num_cols)]
           for i in range(num_rows)]

def board_is_full(board):
    for row in board:
        for element in row:
            if element == '-':
                return False

def insert_chip(board, col, chip_type):
    for row in board:
        if row[col] == '-':
            row[col] = str(chip_type)
            break

def check_if_winner(board, col, row, chip_type):
    count = 0
    current = board[row][col]
    winner_status = False
    for row in board: #This for loop checks to see if there are any horizontal connect 4s
        for element in row:
            if element == current == chip_type:
                count += 1
            else:
                count = 0
            if count == 4:
                break
        if count == 4:
            winner_status = True

    for col in range(0, len(board)):
        pass

    return winner_status


if __name__ == "__main__":
    board = initialize_board(4, 5)
    print(len(board))
    print(len(board[0]))
    insert_chip(board, 1, 'x')
    insert_chip(board, 0, 'x')
    insert_chip(board, 2, 'x')
    print_board(board)
    print(check_if_winner(board, 0, 0, 'x'))

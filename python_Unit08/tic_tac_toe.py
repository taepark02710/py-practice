def make_board():
    
    board = [[" " for _ in range(0, 3)] for _ in range(0, 3)]
    
    return board

def print_board(board):
    
    for row in board:
        print(row)
        
def make_move(board, symbol):
    
    location = input("Enter the row and column: ")
    row = int(location[0])
    col = int(location[1])
    
    board[row][col] = symbol
    
        
        
        

def main():
    board = make_board()
    print_board(board)
    make_move(board, "X")
    print_board(board)
    
    
if __name__ == "__main__":
    main()

    

def is_valid(board, col_val):
    # Check row
    if col_val in board:
        return False
    # Check diagonals
    for i in range(len(board)):
        if len(board) - i == abs(col_val - board[i]):
            return False
    return True

# Board: Array representing indices of queens
def n_queens(n, board = []):
    # If len(board) == n, then we have a complete n queens solution
    if len(board) == n:
        return 1

    count = 0
    # For the next column, consider every row value
    for col_val in range(n):
        # Use is_valid to prune state space tree
        if is_valid(board, col_val):
            count += n_queens(n, board + [col_val])
        
    return count
    
for i in range(10):
    print(n_queens(i))
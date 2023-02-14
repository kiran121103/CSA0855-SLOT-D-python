def is_valid(board):
    n = len(board)
    row_sum = [sum(row) for row in board]
    col_sum = [sum(board[i][j] for i in range(n)) for j in range(n)]
    if sorted(row_sum) != sorted(col_sum) or sorted(row_sum)[0] != n // 2:
        return False
   
    for i in range(n):
        if len(set(board[i])) != 2 or len(set(board[j][i] for j in range(n))) != 2:
            return False
    return True

def min_swaps(board):
    if not is_valid(board):
        return -1
    n = len(board)
    row_swaps = sum(1 for i in range(n) if i % 2 == board[i][0])
    col_swaps = sum(1 for i in range(n) if i % 2 == board[0][i])
    return min(row_swaps, n - row_swaps) // 2 + min(col_swaps, n - col_swaps) // 2

board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
print(min_swaps(board))

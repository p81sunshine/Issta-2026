def totalNQueens(n: int) -> int:
    def addans(board, ans):
        temp = []
        for row in board:
            for j in range(len(row)):
                if row[j] == "Q":
                    temp.append(j + 1)
        ans.append(temp)
    
    def solve(col, board, low, upper, lower, ans, n):
        if col == n:
            addans(board, ans)
            return 
        for row in range(n):
            if low[row] == 0 and upper[n-1+col-row] == 0 and lower[row+col] == 0:
                board[row][col] = "Q"
                low[row] = 1
                upper[n-1+col-row] = 1
                lower[row+col] = 1
                solve(None, board, low, upper, lower, ans, n)
                low[row] = 0
                upper[n-1+col-row] = 0
                lower[row+col] = 0
    
    ans = []        
    board = [[0]*n for i in range(n)]
    low = [0]*n
    upper = [0]*(2*n-1)
    lower = [0]*(2*n-1)
    solve(0, board, low, upper, lower, ans, n)
    return len(ans)
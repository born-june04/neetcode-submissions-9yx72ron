class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ## get all the location of Os
        ## do DFS -> meaning full search within that Os
        ## change temp border Os to T
        ## lastly if O -> X
        ## and T -> O

        rows = len(board)
        cols = len(board[0])

        def dfs(r,c):
            board[r][c] = "T"
            for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr,nc = r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] == "O":
                    dfs(nr,nc)

        for r in range(rows):
            for c in [0,cols-1]:
                if board[r][c] == "O":
                    dfs(r,c)
        
        for c in range(cols):
            for r in [0, rows-1]:
                if board[r][c] == "O":
                    dfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS to mark when visited and start new for new island

        islands = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c): ## row, col
            if r < 0 or r >= rows : return
            if c < 0 or c >= cols : return
            if grid[r][c] == "0" : return
            if (r,c) in visited : return

            visited.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1

        return islands

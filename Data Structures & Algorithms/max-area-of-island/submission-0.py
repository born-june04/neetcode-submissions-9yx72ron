class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        islands_area = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):

            if r<0 or r>=rows: return 0
            if c<0 or c>=cols: return 0
            if grid[r][c] == 0: return 0
            if (r,c) in visited: return 0
            
            visited.add((r,c))

            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1 and (r,c) not in visited:
                    islands_area = max(islands_area, dfs(r,c))
        
        return islands_area
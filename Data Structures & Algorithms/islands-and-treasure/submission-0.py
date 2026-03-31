class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # distance that INF -> 0 and not touch -1
        # bfs start from 0 and update the distance from there

        from collections import deque

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        while queue:
            r,c = queue.popleft()
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+dr,c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc))
        
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS -> store the coordinate of all rotten fruit
        # start from rotten fruit -> meet fresh -> calculate the max distance

        from collections import deque

        queue = deque()
        rows, cols = len(grid), len(grid[0])
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
            time += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return max(0, time-1) ## edge case : [0,0,0] 일때를 대비해서 이렇게 구현됨
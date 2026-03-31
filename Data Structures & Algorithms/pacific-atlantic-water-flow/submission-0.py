class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ## BFS -> we move one point to all the way to the border
        ## start at point -> compare the value if it is lower -> we move to there
        
        from collections import deque

        rows,cols = len(heights), len(heights[0])
        pacific, atlantic = set(),set()

        def bfs(queue, visited):
            while queue:
                r,c = queue.popleft()
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<rows and 0<=nc<cols and\
                    (nr,nc) not in visited and\
                    heights[nr][nc] >= heights[r][c]:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
        
        pac_queue = deque()
        for r in range(rows):
            pac_queue.append((r,0))
            pacific.add((r,0))
            for c in range(cols):
                pac_queue.append((0,c))
                pacific.add((0,c))
        
        atl_queue = deque()
        for r in range(rows):
            atl_queue.append((r,cols-1))
            atlantic.add((r,cols-1))
            for c in range(cols):
                atl_queue.append((rows-1,c))
                atlantic.add((rows-1,c))
        
        bfs(pac_queue,pacific)
        bfs(atl_queue,atlantic)

        return [[r,c] for r,c in pacific if (r,c) in atlantic]


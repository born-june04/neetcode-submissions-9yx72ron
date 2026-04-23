class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # BFS
        # pickup all adjacent
        # mark the connection and when count for new group

        from collections import deque

        visited = set()
        count = 0

        adj = {i:[] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def bfs(node):
            visited.add(node)
            queue = deque([node])
            while queue:
                curr = queue.popleft()
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

        for i in range(n):
            if i not in visited:
                bfs(i) ## visit all connected node
                count += 1
        
        
        return count

            
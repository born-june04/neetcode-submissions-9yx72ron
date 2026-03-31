class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # BFS start with 0
        # store node into visited
        # at the end, if there is cycle -> False
        # visisted != n -> False, since it is not connected
        # else -> True

        from collections import deque

        visited = set()
        visited.add(0)
        queue = deque([(0,-1)]) # current, parent

        adj = {i:[] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        while queue:
            node, parent = queue.popleft()
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue ## going to parent is okay
                if neighbor in visited:
                    return False # cycle
                visited.add(neighbor)
                queue.append((neighbor,node))
        

        return False if len(visited) != n else True
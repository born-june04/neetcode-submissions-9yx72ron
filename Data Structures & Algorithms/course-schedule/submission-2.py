class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 -> 1 -> 0 cycle X
        # DFS to detect whether the system has cycle

        adj = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            adj[a].append(b)
        
        state = [0]*numCourses

        def dfs(node):
            if state[node] == 1: return False ## cycle
            if state[node] == 2: return True

            state[node] = 1 ## visiting
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            
            state[node] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
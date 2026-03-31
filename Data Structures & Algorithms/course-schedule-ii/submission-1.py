class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DFS append all cycle? flow

        adj = {i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            adj[a].append(b)
        
        state = [0]*numCourses
        ans = []

        def dfs(node):
            if state[node] == 1: return False
            if state[node] == 2: return True

            state[node] = 1
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            
            state[node] = 2
            ans.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return ans
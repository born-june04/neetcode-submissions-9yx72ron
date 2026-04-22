class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)

        # def find(x): # finding root(parent) of x
        #     if parent[x] != x:
        #         parent[x] = find(parent[x])
        #     return parent[x]
        def find(x):
            if x == parent[x]:
                return x
            return find(parent[x])
        
        def union(x, y): # combine two groups
            px, py = find(x), find(y)
            if px == py:
                return False # if same group -> its cycle
            
            parent[px] = py
            return True
        
        parent = list(range(n+1))

        for a,b in edges:
            if not union(a,b):
                return [a,b]
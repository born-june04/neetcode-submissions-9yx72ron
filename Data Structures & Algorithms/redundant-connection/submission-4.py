class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        parent = list(range(n+1))
        
        def find(x):
            if x == parent[x]:
                return x
            return find(parent[x])
        
        def union(x, y): # combine two groups
            rep_x, rep_y = find(x), find(y)
            if rep_x == rep_y:
                return False
            
            parent[rep_x] = rep_y
            return True

        for a,b in edges:
            if not union(a,b):
                return [a,b]
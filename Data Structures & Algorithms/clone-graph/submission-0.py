"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # BFS 
        # go to node.val -> append node.neighbors -> go to next node

        from collections import deque

        if not node:
            return None
        
        old_to_new = {}
        queue = deque([node])
        old_to_new[node] = Node(node.val) ## first initial node ## {1:node(1)}

        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val) ## {1:node(1),2:node(2)} -> ## ..{3:node(3)}
                    queue.append(neighbor)
            
                old_to_new[curr].neighbors.append(old_to_new[neighbor])
        
        return old_to_new[node]



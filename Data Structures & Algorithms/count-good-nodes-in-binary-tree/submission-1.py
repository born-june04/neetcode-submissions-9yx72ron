# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node,max_val):
            if not node:
                return 0
            
            good = 1 if node.val >= max_val else 0 ## 내려가면서 판단
            max_val = max(max_val, node.val) ## 내려가면서 업데이트
            ## 올라오면서 합산
            return good + dfs(node.left, max_val) + dfs(node.right, max_val)
        
        return dfs(root, root.val)


        ## BFS
        from collections import deque

        queue = deque([root, root.val])
        good_nodes = 0

        while queue:
            for _ in range(len(queue)):
                node, max_so_far = queue.popleft()
                if node.val >= max_so_far:
                    good_nodes += 1
                max_so_far = max(max_so_far, node.val)
                if node.left:
                    queue.append((node.left, max_so_far))
                if node.right:
                    queue.append((node.right, max_so_far))
        return good_nodes
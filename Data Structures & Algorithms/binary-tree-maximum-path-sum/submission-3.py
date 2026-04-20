# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # bfs because, you can get current node.val and node.left and node.right
        

        # from collections import deque

        # queue = deque([root])
        # ans = float("-inf")
        # while queue:
        #     for _ in range(len(queue)):
        #         node = queue.popleft()

        #         if node.left and node.right:
        #             ans = max(ans, node.val + node.left.val + node.right.val)

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        
        # return ans

        ans = float("-inf")
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            left = max(dfs(node.left), 0) ## 음수 경로는 안쓰는게 낫기때문
            right = max(dfs(node.right), 0)

            ans = max(ans, node.val+left+right)
            return node.val + max(left, right)
        
        dfs(root)
        return ans
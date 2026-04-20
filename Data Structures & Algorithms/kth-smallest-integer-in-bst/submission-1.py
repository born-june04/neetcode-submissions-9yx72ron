# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # dfs -> go all the way down and rank while coming up

        result = []
        def dfs(node):
            
            if not node:
                return
            
            dfs(node.left) ## 왼쪽 먼저 탐색
            result.append(node.val) ## 나 자신 추가
            dfs(node.right) ## 오른쪽 탐색

        dfs(root)
        return result[k-1] ## 0-index라서 k번째면 k-1 index
        
                

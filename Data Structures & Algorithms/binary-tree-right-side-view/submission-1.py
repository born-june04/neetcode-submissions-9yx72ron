# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        from collections import deque

        if not root:
            return []

        queue = deque([root])
        ans = []

        while queue:
            level_size = len(queue)
            for i in range(len(queue)):
                node = queue.popleft() # same level node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == level_size - 1: ## 현재 레벨의 마지막 노드 == 오른쪽에서만 보이는 노드
                    ans.append(node.val)
        
        return ans
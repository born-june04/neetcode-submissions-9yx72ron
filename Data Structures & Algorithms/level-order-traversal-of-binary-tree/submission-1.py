# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Tree structure

        # Each node operates like this,
        # we can also use depth value
        # 1 = node.val / 2 = node.left, 3 = node.right
        # 2 = node.val / 4 = node.left, 5 = node.right
        # 3 = node.val / 6 = node.left, 7 = node.right

        # 1 -> 2 -> 4 -> 5 -> 3 -> 6 -> 7
        # stage = 0
        # ans = {}
        # def dfs(node, stage:int, ans:dict):
            
        #     if not node:
        #         stage = 1
        #         return ans

        #     print(ans)
        #     if stage not in ans:
        #         ans[stage] = [node.val]
        #     else:
        #         ans[stage].append(node.val)
            
        #     stage += 1
        #     ans = dfs(node.left, stage, ans)
        #     ## {0 : [1], 1 : [2], 2 : [4]} ## stage = 1
        #     ans = dfs(node.right, stage, ans)
        #     return ans
        
        # dfs(root, stage, ans)

        # return [v for v in ans.values()]

        ## BFS

        from collections import deque

        queue = deque([root]) # 시작 노드 넣기
        ans = []
        
        if root is None:
            return ans

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(level)

        return ans

                

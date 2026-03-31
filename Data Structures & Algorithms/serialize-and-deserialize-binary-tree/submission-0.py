# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    from collections import deque
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        if not root:
            return ""

        queue = deque([root])
        result = [str(root.val)]

        while queue:
            node = queue.popleft()

            if node.left:
                result.append(str(node.left.val))
                queue.append(node.left)
            else:
                result.append("_")

            if node.right:
                result.append(str(node.right.val))
                queue.append(node.right)
            else:
                result.append("_")
        
        return ",".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if not data:
            return None

        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(nodes):
            node = queue.popleft()

            if nodes[i] != "_":
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            
            i += 1

            if nodes[i] != "_":
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1
        
        return root

            
            

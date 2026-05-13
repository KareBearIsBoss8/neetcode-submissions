# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = [root]
        res = []

        while queue:
            length = len(queue)
            layer = []
            
            for i in range(length):
                node = queue.pop(0)
            
                if node is not None:
                    layer.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if layer:
                res.append(layer[-1])
        
        return res
            


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = [root]
        res = []

        while queue:
            length = len(queue)
            group = []
            
            for i in range(length):
                node = queue.pop(0)
            
                if node is not None:
                    group.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if group:
                res.append(group)
        
        return res

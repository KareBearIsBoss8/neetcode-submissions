# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, root, minimum, maximum):
        if root is None:
            return True
        
        if root.val <= minimum or root.val >= maximum:
            return False

        if root.left and root.right is None:
            return self.helper(root.left, minimum, root.val)
        elif root.right and root.left is None:
            return self.helper(root.right, root.val, maximum)
        
        return (self.helper(root.left, minimum, root.val) and self.helper(root.right, root.val, maximum))
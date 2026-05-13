# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        height_left = self.maxHeight(root.left)
        height_right = self.maxHeight(root.right)

        if abs(height_left - height_right) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def maxHeight(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0
        
        return 1+max(self.maxHeight(root.left), self.maxHeight(root.right))
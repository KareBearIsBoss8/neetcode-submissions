# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = self.inorder(root, [])
        
        return nodes[k-1]
    
    def inorder(self, root: Optional[TreeNode], nodes: List):
        if not root:
            return nodes
        
        if root:
            self.inorder(root.left, nodes)
            nodes.append(root.val)
            self.inorder(root.right, nodes)
        
        return nodes
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepthUtil(self, root: Optional[TreeNode], height: int) -> int:
        if not root:
            return 0
        
        return 1 + max( self.maxDepthUtil(root.left, height+1) , self.maxDepthUtil(root.right, height+1) ) 
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.maxDepthUtil(root, 0)
        
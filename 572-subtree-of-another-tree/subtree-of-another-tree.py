# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isIdentical(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot or root.val != subRoot.val:
            return False
        
        return self.isIdentical(root.left, subRoot.left) and self.isIdentical(root.right, subRoot.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False
        

        is_subtree = False
        if root.val == subRoot.val:
            is_subtree = self.isIdentical(root.left, subRoot.left) and self.isIdentical(root.right, subRoot.right)
        
        if is_subtree:
            return True
        

        return  self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        

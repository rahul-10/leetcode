# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_diameter = 0

    def diameterOfBinaryTreeUtil(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.diameterOfBinaryTreeUtil(root.left)
        right = self.diameterOfBinaryTreeUtil(root.right)
        self.max_diameter = max(self.max_diameter, left+right+1)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameterOfBinaryTreeUtil(root)
        return self.max_diameter -1
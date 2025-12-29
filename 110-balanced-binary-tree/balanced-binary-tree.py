# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalancedUtil(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        if not root:
            return True, 0
        
        is_left, left = self.isBalancedUtil(root.left)

        if not is_left:
            return is_left, left
        
        is_right, right = self.isBalancedUtil(root.right)
        
        if not is_right:
            return is_right, right
        
        print('left: ', left, ', right: ', right)

        return abs(right-left) <= 1, 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, _ = self.isBalancedUtil(root)

        return balanced
        
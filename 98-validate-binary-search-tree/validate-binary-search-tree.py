# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        max_till_now = float("-inf")
        def inOrderTraversal(root: Optional[TreeNode]) -> Optional[int]:
            nonlocal max_till_now

            if not root:
                return True
            
            left = inOrderTraversal(root.left)
            if left is False or max_till_now >= root.val:
                return False
            
            max_till_now = root.val

            right = inOrderTraversal(root.right)
            
            return False if right is False else True

        return inOrderTraversal(root)
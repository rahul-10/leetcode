# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        max_till_now = float("-inf")
        if max_till_now >= root.val:
                return False
        # print('1. max_till_now: ', max_till_now)
        def inOrderTraversal(root: Optional[TreeNode]) -> Optional[int]:
            nonlocal max_till_now

            if not root:
                return None
            
            left = inOrderTraversal(root.left)
            if left == False or max_till_now >= root.val:
                return False
            
            max_till_now = root.val

            right = inOrderTraversal(root.right)
            
            return False if right == False else True

        return inOrderTraversal(root)
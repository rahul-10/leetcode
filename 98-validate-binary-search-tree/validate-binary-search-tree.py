# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # max_till_now = float("-inf")
        # def inOrderTraversal(root: Optional[TreeNode]) -> bool:
        #     nonlocal max_till_now

        #     if not root:
        #         return True
            
        #     left = inOrderTraversal(root.left)
        #     if left is False or max_till_now >= root.val:
        #         return False
            
        #     max_till_now = root.val

        #     right = inOrderTraversal(root.right)
            
        #     return False if right is False else True

        # return inOrderTraversal(root)

        def dfs(node, low, high):
            if not node:
                return True

            # current node must be strictly between bounds
            if not (low < node.val < high):
                return False

            return (
                dfs(node.left, low, node.val) and
                dfs(node.right, node.val, high)
            )

        return dfs(root, float("-inf"), float("inf"))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.index = 0

    def kthSmallestUtil(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        left = self.kthSmallestUtil(root.left, k)
        if isinstance(left, int):
            return left
        self.index += 1
        if self.index == k:
            return root.val

        right = self.kthSmallestUtil(root.right, k)
        if isinstance(right, int):
            return right

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.kthSmallestUtil(root, k)
        
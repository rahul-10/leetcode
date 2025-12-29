# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def kthSmallestUtil(self, root: Optional[TreeNode], k: int) -> Optional[int]:
        if not root:
            return None
        
        left = self.kthSmallestUtil(root.left, k)

        if left is not None:
            return left
        
        # print('self.count: ', self.count, 'root: ', root.val)
        self.count = self.count+1

        if self.count == k:
            return root.val

        right = self.kthSmallestUtil(root.right, k)

        return right

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        return self.kthSmallestUtil(root, k)
        
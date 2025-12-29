# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

MIN_NUM = -(2**31) - 1
MAX_NUM = 2**31

class Solution:

    def isValidBSTUtil(self, root: Optional[TreeNode], min_num: int, max_num: int) -> bool:

        if not root:
            return True
        if min_num >= root.val or root.val >= max_num:
            return False

        return self.isValidBSTUtil(root.left, min_num, root.val) and self.isValidBSTUtil(root.right, root.val, max_num)  


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # print('MIN_NUM: ---> ', MIN_NUM, ', MAX_NUM: ', MAX_NUM)
        return  self.isValidBSTUtil(root, MIN_NUM, MAX_NUM)
 
        
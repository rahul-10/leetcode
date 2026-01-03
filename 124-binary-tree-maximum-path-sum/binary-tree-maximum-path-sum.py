# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        min_num = -100000
        self.max_sum = min_num



        def dfs(root: Optional[TreeNode]):
            if not root:
                return min_num
            
            left = dfs(root.left)
            right = dfs(root.right)

            curr_max = max(left+right+root.val, root.val)
            curr_max = max(curr_max, left)
            curr_max = max(curr_max, right)
            curr_max = max(curr_max, right + root.val)
            curr_max = max(curr_max, left + root.val)
            
            # print("self.max_sum: ", self.max_sum, ', curr_max: ', curr_max)

            self.max_sum = max(self.max_sum, curr_max)
            
            return  root.val + max(0, max(left, right))

        dfs(root)
        return self.max_sum
        
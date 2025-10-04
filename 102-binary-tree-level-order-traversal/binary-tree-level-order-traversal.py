from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)
        count = 1
        level = []
        new_count=0
        while len(queue):
            temp = queue.popleft()
            level.append(temp.val)
            
            if temp.left:
                queue.append(temp.left)
                new_count += 1
            if temp.right:
                queue.append(temp.right)
                new_count += 1
            
            count -= 1
            if count == 0:
                res.append(level)
                level = []
                count = new_count
                new_count = 0

        return res
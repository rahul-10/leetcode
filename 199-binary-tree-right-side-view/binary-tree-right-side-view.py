from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return result

        queue = deque()
        queue.append(root)
        while queue:
            result.append(queue[0].val)
            for i in range(len(queue)):
                temp = queue.popleft()
                if temp.right:
                    queue.append(temp.right)
                if temp.left:
                    queue.append(temp.left)

        return result

        
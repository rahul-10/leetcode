# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_hight = -1

    def rightSigheViewUtil(self, root:Optional[TreeNode], curr_height: int, right_view: List[int]) -> None:
        if not root:
            return 
        
        if self.max_hight < curr_height:
            self.max_hight = curr_height
            right_view.append(root.val)
        
        self.rightSigheViewUtil(root=root.right, curr_height=curr_height+1, right_view=right_view)

        self.rightSigheViewUtil(root=root.left, curr_height=curr_height+1, right_view=right_view)


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
        self.rightSigheViewUtil(root, 0, right_view)
        return right_view
        
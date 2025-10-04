# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.preorder_index = 0

    def ger_inorder_index(self, inorder: List[int], start: int, end: int, value: int) -> int:
        for i in range(start, end+1):
            if inorder[i] == value:
                return i
        return -1

    def buildTreeUtil(self, preorder: List[int], inorder: List[int], start: int, end: int) -> Optional[TreeNode]:
        if self.preorder_index>= len(preorder):
            return None
        
        index = self.ger_inorder_index(inorder, start, end, preorder[self.preorder_index])
        
        if index == -1:
            return None

        root = TreeNode(preorder[self.preorder_index])
        
        self.preorder_index += 1

        root.left = self.buildTreeUtil(preorder, inorder, start, index-1)
        

        root.right = self.buildTreeUtil(preorder, inorder,index+1, end)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeUtil(preorder, inorder, 0, len(preorder)-1)
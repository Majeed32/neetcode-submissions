# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(root):
            if not root:
                return 0,True
            l_height, l_balanced = checkHeight(root.left)
            r_height, r_balanced =checkHeight(root.right)
            is_balanced = l_balanced and r_balanced and abs(l_height - r_height) <= 1
            return 1 + max(l_height, r_height), is_balanced
        return checkHeight(root)[1]
        
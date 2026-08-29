# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0, True
            left, l_balanced = dfs(root.left)
            right, r_balanced = dfs(root.right)
            balanced = l_balanced and r_balanced and abs(left - right) <= 1
            return 1 + max(left, right), balanced
        return dfs(root)[1]
        
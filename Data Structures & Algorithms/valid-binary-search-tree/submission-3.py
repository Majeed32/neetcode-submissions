# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        def dfs(root):
            nonlocal prev
            if not root:
                return True
            left = dfs(root.left)
            if prev and root.val <= prev.val:
                return False
            prev = root
            right = dfs(root.right)
            return left and right
        return dfs(root)

        
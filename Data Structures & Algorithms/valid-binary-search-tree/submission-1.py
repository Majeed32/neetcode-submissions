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
            if not dfs(root.left):
                return False
            if prev and root.val <= prev.val:
                return False
            prev = root
            return dfs(root.right)
        return dfs(root)

        